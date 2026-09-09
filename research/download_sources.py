"""Retrieve exact public files used in the two analyses; no account required."""
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import argparse, hashlib, json

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path,default=Path('local-data'));args=parser.parse_args()
    source=Path(__file__).resolve().parent
    manifest=json.loads((source/'download_manifest.json').read_text())
    def fetch(record):
        path=args.destination/'physionet'/record['path'];path.parent.mkdir(parents=True,exist_ok=True)
        if path.exists(): data=path.read_bytes()
        else:
            with urlopen(record['url'],timeout=45) as response:data=response.read()
            if hashlib.sha256(data).hexdigest()!=record['sha256']:raise ValueError('Source changed: '+record['path'])
            path.write_bytes(data)
        if hashlib.sha256(data).hexdigest()!=record['sha256']:raise ValueError('Local checksum mismatch: '+str(path))
    with ThreadPoolExecutor(max_workers=4) as pool:list(pool.map(fetch,manifest['files']))
    report=json.loads((source/'antidote_results.json').read_text());path=args.destination/'antidote'/'data.csv';path.parent.mkdir(parents=True,exist_ok=True)
    data=path.read_bytes() if path.exists() else urlopen(report['data_url'],timeout=45).read()
    if hashlib.sha256(data).hexdigest()!=report['raw_sha256']:raise ValueError('ANTIDOTE source changed; inspect its version before reanalysis.')
    path.write_bytes(data)
    print('Downloaded and verified 179 PhysioNet files and the ANTIDOTE numerical table.')

if __name__=='__main__':main()
