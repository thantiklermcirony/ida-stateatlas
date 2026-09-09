import unittest, math
from ida_capture import Decoder, decode_frame, process, signed24, validate_config

CONFIG={'sample_rate_hz':250,'reference_v':4.5,'gains':[24]*8,'channel_labels':['Fp1','Fp2','F7','F8','O1','O2','VEOG','HEOG']}
def frame(counter,counts=None,footer=0xc0):
    return bytes([0xa0,counter%256])+b''.join(int(x).to_bytes(3,'big',signed=True) for x in (counts or [1,-1,100,-100,10,-10,1000,-1000]))+bytes(6)+bytes([footer])

class CaptureTests(unittest.TestCase):
    def test_signed_boundaries(self):
        self.assertEqual(signed24(bytes.fromhex('800000')),-8388608)
        self.assertEqual(signed24(bytes.fromhex('7fffff')),8388607)
        self.assertEqual(signed24(bytes.fromhex('ffffff')),-1)
    def test_scale_and_channel_gains(self):
        c={**CONFIG,'gains':[1,2,4,6,8,12,24,24]}
        d=decode_frame(frame(1,[100]*8),c)
        self.assertAlmostEqual(d['microvolts'][0]/d['microvolts'][6],24)
        self.assertAlmostEqual(d['microvolts'][6],2.23517444553,places=8)
    def test_every_chunk_boundary(self):
        wire=b'boot\r\n$$$'+b''.join(frame(i) for i in range(4))
        for split in range(len(wire)+1):
            d=Decoder(CONFIG);f=d.feed(wire[:split])+d.feed(wire[split:])
            self.assertEqual([x['counter'] for x in f],[0,1,2,3])
            self.assertEqual(d.discarded_bytes,9)
    def test_resynchronizes_after_bad_footer(self):
        d=Decoder(CONFIG);bad=bytearray(frame(3));bad[-1]=0
        out=d.feed(bytes(bad)+frame(4));self.assertEqual([f['counter'] for f in out],[4])
        self.assertEqual(d.discarded_bytes,33)
    def test_wrap_and_gap(self):
        d=Decoder(CONFIG);f=d.feed(frame(255)+frame(0)+frame(3))
        self.assertEqual(f[1]['continuity'],'contiguous');self.assertEqual(f[2]['minimum_missing_if_forward'],2)
    def test_duplicate_is_not_silent(self):
        f=Decoder(CONFIG).feed(frame(5)+frame(5))
        self.assertEqual(f[-1]['continuity'],'duplicate_or_256_multiple_loss')
    def test_partial_tail_retained(self):
        r=process(frame(0)+frame(1)[:9],CONFIG)
        self.assertEqual(r['summary']['frames'],1);self.assertEqual(r['summary']['trailing_bytes'],9)
    def test_unknown_aux_not_misread_as_acceleration(self):
        self.assertIsNone(decode_frame(frame(0,footer=0xc6),CONFIG)['accelerometer_raw'])
    def test_invalid_configuration(self):
        for c in [{**CONFIG,'gains':[24]*7},{**CONFIG,'reference_v':float('nan')},{**CONFIG,'sample_rate_hz':125},{**CONFIG,'channel_labels':['x']*8}]:
            with self.assertRaises(ValueError):validate_config(c)
    def test_flatline_rejected(self):
        r=process(b''.join(frame(i,[0]*8) for i in range(1000)),CONFIG)
        self.assertEqual(r['summary']['usable_windows'],0)
    def test_rails_rejected(self):
        r=process(b''.join(frame(i,[8388607 if i%2 else -8388608]*8) for i in range(1000)),CONFIG)
        self.assertEqual(r['summary']['usable_windows'],0)
    def test_synthetic_clean_window(self):
        r=process(b''.join(frame(i,[round(1000*math.sin(i*.2513+j)) for j in range(8)]) for i in range(1000)),CONFIG)
        self.assertEqual(r['summary']['usable_windows'],1)
    def test_discontinuity_invalidates_window(self):
        r=process(b''.join(frame(i+(1 if i>100 else 0),[round(1000*math.sin(i*.2513+j)) for j in range(8)]) for i in range(1000)),CONFIG)
        self.assertEqual(r['summary']['usable_windows'],0)

if __name__=='__main__':unittest.main()
