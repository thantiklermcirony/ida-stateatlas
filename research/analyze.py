"""Exploratory, participant-held-out IDA measurement screening. NumPy only."""
from pathlib import Path
import argparse, csv, hashlib, json, platform
import numpy as np

ALPHAS=[0.1,1.,10.,100.,1000.]
PHASES={'wb':(0,360),'s1':(360,720),'r1':(720,1080),'s2':(1080,1440),'r1last':(1020,1080),'r1early':(720,840),'r1mid':(840,960)}
PERF=['wb_od','s1_od','r1last_od']
SNAP=PERF+['HR_last','EDA_last']
BEH=['r1early_od','r1mid_od']
RES=['HR_residue','EDA_residue']
MODELS={'performance':PERF,'snapshot':SNAP,'generic_history':SNAP+['HR_mean_delta','EDA_mean_delta'],'residue':SNAP+RES,'behavioral_history':PERF+BEH,'combined_baseline':SNAP+BEH,'combined_residue':SNAP+BEH+RES}

def elapsed(s):
    parts=list(map(float,s.split(':')))
    return sum(v*60**i for i,v in enumerate(parts[::-1]))

def physiology(path,tag,shift):
    vals=np.array([float(s.strip()) for s in path.read_text().splitlines() if s.strip()])
    start,rate=vals[:2]
    assert rate>0
    v=vals[2:]
    t=start+np.arange(len(v))/rate-tag+shift
    return t,v,rate

def features(raw,shift=0):
    rows=[]; audits=[]
    for path in sorted((raw/'MATB-II').glob('*resman.csv')):
        pid=path.name[:3]; audit={'id':pid,'shift_s':shift,'exclude':[],'flags':[]}; row={'id':pid}
        try:
            with path.open(encoding='utf-8-sig',newline='') as f: data=list(csv.DictReader(f))
            t=np.array([elapsed(d['ELAPSED_TIME']) for d in data])
            diff=np.array([[float(d['DIFF_A']),float(d['DIFF_B'])] for d in data])
            tanks=np.array([[float(d['TANK_A']),float(d['TANK_B'])] for d in data])
            assert np.allclose(diff,tanks-2500), 'DIFF and tank values disagree'
            if np.any(np.diff(t)<=0): audit['exclude'].append('nonmonotone task times')
            audit['task_rows']=len(t); audit['task_end_s']=float(t[-1]); audit['phase_counts']={}
            for name,(lo,hi) in PHASES.items():
                mask=(t>=lo)&(t<hi)&np.all(np.isfinite(diff),axis=1)
                audit['phase_counts'][name]=int(mask.sum())
                if mask.sum()<0.8*(hi-lo)/10: audit['exclude'].append('task coverage '+name)
                row[name+'_od']=float(np.sqrt(np.mean(diff[mask]**2))) if mask.any() else None
            tagpath=raw/'PPG'/pid/'tags.csv'
            tags=[float(s) for s in tagpath.read_text().splitlines() if s.strip()]
            audit['tag_count']=len(tags)
            if len(tags)!=1: raise ValueError('Working Baseline tag missing or ambiguous')
            for channel in ['HR','EDA']:
                pt,pv,rate=physiology(raw/'PPG'/pid/(channel+'.csv'),tags[0],shift)
                valid=np.isfinite(pv)&((pv>0) if channel=='HR' else (pv>=0))
                values=np.log1p(np.maximum(pv,0)) if channel=='EDA' else pv
                slices={}
                for name in ['wb','r1','r1last']:
                    lo,hi=PHASES[name]; mask=(pt>=lo)&(pt<hi)&valid
                    count=int(mask.sum()); audit[f'{channel}_{name}_fraction']=count/((hi-lo)*rate)
                    if count<0.8*(hi-lo)*rate: audit['exclude'].append(channel+' coverage '+name)
                    slices[name]=values[mask]
                if any(len(v)==0 for v in slices.values()): raise ValueError('empty physiological interval')
                base=float(np.mean(slices['wb'])); sd=float(np.std(slices['wb']))
                if np.ptp(slices['wb'])==0 or np.ptp(slices['r1'])==0:
                    audit['flags'].append(channel+' flat interval')
                floor=1.0 if channel=='HR' else .01
                row[channel+'_last']=float(np.mean(slices['r1last']))
                row[channel+'_mean_delta']=float(np.mean(slices['r1'])-base)
                row[channel+'_residue']=float(np.mean(np.maximum(np.abs(slices['r1']-base)-sd,0))/max(sd,floor))
                row[channel+'_baseline_mean']=base; row[channel+'_baseline_sd']=sd
                row[channel+'_record_start']=float(pt[0]); row[channel+'_record_end']=float(pt[-1])
                ibi=(raw/'PPG'/pid/'IBI.csv').read_text().splitlines()
                audit['ibi_rows']=max(0,len([s for s in ibi if s.strip()])-1)
        except Exception as e:
            audit['exclude'].append(str(e))
        audit['eligible']=not audit['exclude']
        if audit['eligible']: rows.append(row)
        audits.append(audit)
    return rows,audits

def fit_predict(x,y,z,alpha):
    mean=x.mean(axis=0); sd=x.std(axis=0); sd=np.where(sd<1e-12,1.,sd)
    a=(x-mean)/sd; b=(z-mean)/sd; ym=y.mean()
    coef=np.linalg.solve(a.T@a+alpha*np.eye(x.shape[1]),a.T@(y-ym))
    return ym+b@coef

def nested_loo(x,y):
    n=len(y); preds=np.zeros(n); selected=[]
    for held in range(n):
        outer=np.arange(n)!=held; xt=x[outer]; yt=y[outer]
        losses=[]
        for alpha in ALPHAS:
            errors=[]
            for inner in range(n-1):
                keep=np.arange(n-1)!=inner
                p=fit_predict(xt[keep],yt[keep],xt[inner:inner+1],alpha)[0]
                errors.append((p-yt[inner])**2)
            losses.append(float(np.mean(errors)))
        alpha=ALPHAS[int(np.argmin(losses))]
        preds[held]=fit_predict(xt,yt,x[held:held+1],alpha)[0]; selected.append(alpha)
    return preds,selected

def evaluate(rows):
    y=np.array([r['s2_od'] for r in rows]); n=len(y)
    predictions={'training_mean':(y.sum()-y)/(n-1),'stress1_persistence':np.array([r['s1_od'] for r in rows])}
    penalties={}
    for name,cols in MODELS.items():
        predictions[name],penalties[name]=nested_loo(np.array([[r[c] for c in cols] for r in rows]),y)
    metrics={name:{'mae':float(np.mean(np.abs(p-y))),'rmse':float(np.sqrt(np.mean((p-y)**2)))} for name,p in predictions.items()}
    rng=np.random.default_rng(20260907); indices=rng.integers(0,n,size=(10000,n)); comparisons={}
    for label,a,b in [('primary_residue_increment','combined_baseline','combined_residue'),('residue_over_snapshot','snapshot','residue'),('residue_over_generic','generic_history','residue'),('behavioral_history_increment','performance','behavioral_history')]:
        delta=np.abs(predictions[a]-y)-np.abs(predictions[b]-y)
        draws=delta[indices].mean(axis=1)
        comparisons[label]={'baseline':a,'candidate':b,'mae_improvement':float(delta.mean()),'relative_mae_improvement_percent':float(100*delta.mean()/metrics[a]['mae']),'descriptive_fixed_oof_bootstrap_95_range':np.quantile(draws,[.025,.975]).tolist(),'participants_improved':int((delta>0).sum()),'n':n}
    saved=[{'id':r['id'],'actual_s2_od':float(y[i]),**{k:float(v[i]) for k,v in predictions.items()},'selected_penalties':{k:v[i] for k,v in penalties.items()}} for i,r in enumerate(rows)]
    return {'n':n,'metrics':metrics,'comparisons':comparisons,'predictions':saved}

def self_check():
    assert elapsed('01:40.1')==100.1
    x=np.array([[0.],[1.],[2.],[3.]]); y=np.array([1.,3.,5.,7.])
    assert abs(fit_predict(x,y,np.array([[4.]]),1e-10)[0]-9)<1e-8
    assert np.allclose(fit_predict(x,np.ones(4)*3,np.array([[4.]]),10),3)
    # Held-out target cannot affect its own prediction, including tuning.
    p,_=nested_loo(x,y); altered=y.copy(); altered[0]=10000
    q,_=nested_loo(x,altered); assert abs(p[0]-q[0])<1e-10

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--raw',type=Path,required=True); parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args(); args.out.mkdir(parents=True,exist_ok=True); self_check()
    allrows={}; allaudits={}
    for shift in [0,-10,10]:
        allrows[shift],allaudits[shift]=features(args.raw,shift)
    common=set.intersection(*[{r['id'] for r in rows} for rows in allrows.values()])
    result={'protocol':'IDA_Discovery_Protocol.md','analysis_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python':platform.python_version(),'numpy':np.__version__,'models':MODELS,'nominal':None,'alignment_sensitivity':{},'qc':allaudits,'tests':'elapsed, ridge exact limit, constant outcome, held-out-target independence passed'}
    nominal=allrows[0]
    if len(nominal)<10: raise RuntimeError('Too few eligible participants: '+json.dumps(allaudits[0]))
    result['nominal']=evaluate(nominal)
    for shift in [-10,0,10]:
        rows=[r for r in allrows[shift] if r['id'] in common]
        result['alignment_sensitivity'][str(shift)]=evaluate(rows)
    flagged={a['id'] for a in allaudits[0] if a['flags']}
    if flagged:
        result['exclude_flat_sensitivity']=evaluate([r for r in nominal if r['id'] not in flagged])
    (args.out/'participant_features.json').write_text(json.dumps(nominal,indent=2))
    (args.out/'results.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({'n':result['nominal']['n'],'metrics':result['nominal']['metrics'],'comparisons':result['nominal']['comparisons'],'excluded':[a for a in allaudits[0] if not a['eligible']],'flagged':[a for a in allaudits[0] if a['flags']]},indent=2))

if __name__=='__main__': main()
