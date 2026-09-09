"""Generate and test synthetic transport fixtures; no participant data."""
from pathlib import Path
import math,json,hashlib
from ida_capture import process
from test_capture import frame,CONFIG

def main():
    out=Path(__file__).resolve().parents[1]/'bench';out.mkdir(exist_ok=True)
    cases={}
    for name in ['clean','dropout','flat','rail','large_artifact']:
        parts=[]
        for i in range(3000):
            if name=='dropout' and i==1200:continue
            counts=[round(1000*math.sin(2*math.pi*10*i/250+j)) for j in range(8)]
            if name=='flat':counts=[0]*8
            if name=='rail' and i%500==0:counts=[8388607]*8
            if name=='large_artifact' and i%500<20:counts[0]+=30000
            parts.append(frame(i,counts))
        raw=b''.join(parts);r=process(raw,CONFIG)
        cases[name]={'raw_sha256':r['raw_sha256'],**r['summary']}
        if name=='clean':
            (out/'synthetic_clean.bin').write_bytes(raw)
            (out/'synthetic_config.json').write_text(json.dumps(CONFIG,indent=2))
    result={'fixture':'Invented waveforms and faults; not human EEG or physical hardware validation','cases':cases,
            'calculations':{'bytes_per_second':33*250,'megabytes_per_hour_decimal':33*250*3600/1e6,
              'uart_bits_per_second_8n1':33*250*10,'microvolts_per_count_gain24':4.5e6/24/(2**23-1)},
            'code_sha256':hashlib.sha256((Path(__file__).parent/'ida_capture.py').read_bytes()).hexdigest()}
    (out/'results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
