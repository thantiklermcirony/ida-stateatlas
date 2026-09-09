"""Offline Cyton packet decoder and engineering QC; never operates a device.

Input: recorded binary bytes plus a per-channel gain configuration.
Output: raw counts, scaled microvolts, continuity flags, and provenance.
Packet contract: https://docs.openbci.com/Cyton/CytonDataFormat/
"""
from pathlib import Path
import argparse, hashlib, json, math, statistics

VALID_GAINS={1,2,4,6,8,12,24}

def validate_config(c):
    if c.get('sample_rate_hz') != 250:
        raise ValueError('R1 decoder contract is nominal 250 Hz only; no Daisy or rate substitution.')
    gains=c.get('gains')
    if not isinstance(gains,list) or len(gains)!=8 or any(type(x) is not int or x not in VALID_GAINS for x in gains):
        raise ValueError('Eight verified integer gains are required.')
    if type(c.get('reference_v')) not in (int,float) or not math.isfinite(c['reference_v']) or not 0<c['reference_v']<=5:
        raise ValueError('A finite verified reference voltage is required.')
    labels=c.get('channel_labels')
    if not isinstance(labels,list) or len(labels)!=8 or any(not isinstance(x,str) or not x for x in labels) or len(set(labels))!=8:
        raise ValueError('Eight unique channel labels required.')
    return c

def signed24(b):
    if len(b)!=3: raise ValueError('Exactly three bytes required.')
    return int.from_bytes(b,'big',signed=True)

def decode_frame(b,c):
    if len(b)!=33 or b[0]!=0xa0 or b[32]&0xf0!=0xc0: raise ValueError('Invalid frame boundary.')
    counts=[signed24(b[2+i*3:5+i*3]) for i in range(8)]
    uv=[x*c['reference_v']*1e6/g/(2**23-1) for x,g in zip(counts,c['gains'])]
    return {'counter':b[1],'counts':counts,'microvolts':uv,'footer':b[32],
            'aux_hex':b[26:32].hex(),
            'accelerometer_raw':[int.from_bytes(b[i:i+2],'big',signed=True) for i in (26,28,30)] if b[32]==0xc0 else None,
            'aux_interpretation':'accelerometer raw only; physical scaling requires configuration' if b[32]==0xc0 else 'specialized auxiliary format preserved but not decoded'}

class Decoder:
    def __init__(self,config):
        self.config=validate_config(config);self.buffer=bytearray();self.previous=None
        self.discarded_bytes=0;self.total_frames=0
    def feed(self,data):
        self.buffer.extend(data);out=[]
        while len(self.buffer)>=33:
            if self.buffer[0]!=0xa0 or self.buffer[32]&0xf0!=0xc0:
                del self.buffer[0];self.discarded_bytes+=1;continue
            raw=bytes(self.buffer[:33]);del self.buffer[:33]
            f=decode_frame(raw,self.config)
            delta=None if self.previous is None else (f['counter']-self.previous)%256
            f['continuity']='start' if delta is None else 'contiguous' if delta==1 else 'duplicate_or_256_multiple_loss' if delta==0 else 'gap_or_reset'
            f['counter_delta_mod256']=delta
            f['minimum_missing_if_forward']=delta-1 if delta is not None and delta>1 else 0
            f['frame_index']=self.total_frames
            # Deliberately do not invent acquisition timestamps from arrival or index.
            self.previous=f['counter'];self.total_frames+=1;out.append(f)
        return out

def quality(frames,config):
    if not frames: return {'usable':False,'reasons':['empty window'],'channels':[]}
    reasons=[];chs=[]
    if any(f['continuity'] not in ('start','contiguous') for f in frames): reasons.append('counter discontinuity')
    if len(frames)<1000: reasons.append('shorter than proposed four-second window')
    for ch,label in enumerate(config['channel_labels']):
        x=[f['microvolts'][ch] for f in frames];raw=[f['counts'][ch] for f in frames]
        if not all(math.isfinite(v) for v in x):
            chs.append({'label':label,'status':'invalid'});reasons.append('nonfinite samples');continue
        rail=sum(abs(v)>=.98*(2**23-1) for v in raw)/len(raw)
        span=max(x)-min(x);sd=statistics.pstdev(x)
        flags=[]
        if rail>0: flags.append('near ADC rail')
        if span<.1: flags.append('flatline candidate')
        # A simple acquisition screen, not a neural/ocular source classifier.
        if ch<6 and span>500: flags.append('large amplitude candidate')
        chs.append({'label':label,'std_uv':sd,'peak_to_peak_uv':span,'rail_fraction':rail,'flags':flags})
        reasons.extend(label+': '+flag for flag in flags)
    return {'usable':not reasons,'reasons':reasons,'channels':chs,
            'scope':'Engineering candidate thresholds; no clinical validity, no artifact-free certification.'}

def process(binary,config):
    d=Decoder(config);frames=[]
    for start in range(0,len(binary),257): frames.extend(d.feed(binary[start:start+257]))
    windows=[{'start_frame':i,'quality':quality(frames[i:i+1000],config)} for i in range(0,len(frames),1000)]
    return {'config':config,'raw_sha256':hashlib.sha256(binary).hexdigest(),'frames':frames,
            'summary':{'frames':len(frames),'discarded_bytes':d.discarded_bytes,'trailing_bytes':len(d.buffer),
              'continuity_issues':sum(f['continuity'] not in ('start','contiguous') for f in frames),
              'usable_windows':sum(w['quality']['usable'] for w in windows),'windows':len(windows)},
            'quality_windows':windows,
            'limitations':['No CRC exists in this frame contract; an in-frame bit flip can remain undetected.',
              'One-byte counter cannot detect all wraparound/reset/loss cases.',
              'No physical acquisition timestamps supplied; sample indices are not synchronized event times.',
              'No brain-state or intervention model is fitted.']}

def main():
    p=argparse.ArgumentParser();p.add_argument('--binary',type=Path,required=True);p.add_argument('--config',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    c=validate_config(json.loads(a.config.read_text(encoding='utf-8')))
    result=process(a.binary.read_bytes(),c);a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result['summary']))
if __name__=='__main__':main()
