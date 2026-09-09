"""Secondary reanalysis of a published randomized analogue-trauma experiment."""
import argparse, csv, hashlib, json
from pathlib import Path
import numpy as np
from analyze import ALPHAS, fit_predict

def number(s):
    try:return float(s)
    except (ValueError,TypeError):return np.nan

def prepared_predict(x,y,z,alpha):
    med=np.array([np.nanmedian(x[:,j]) if np.isfinite(x[:,j]).any() else 0. for j in range(x.shape[1])])
    def transform(a): return np.concatenate([np.where(np.isfinite(a),a,med),~np.isfinite(a)],axis=1).astype(float)
    return fit_predict(transform(x),y,transform(z),alpha)

def loo(x,y):
    out=np.zeros(len(y)); penalties=[]
    for i in range(len(y)):
        keep=np.arange(len(y))!=i; a=x[keep]; b=y[keep]; errors=[]
        for alpha in ALPHAS:
            e=[]
            for j in range(len(b)):
                inner=np.arange(len(b))!=j
                e.append((prepared_predict(a[inner],b[inner],a[j:j+1],alpha)[0]-b[j])**2)
            errors.append(np.mean(e))
        alpha=ALPHAS[int(np.argmin(errors))]; penalties.append(alpha)
        out[i]=prepared_predict(a,b,x[i:i+1],alpha)[0]
    return out,penalties

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--data',type=Path,required=True);parser.add_argument('--out',type=Path,required=True);args=parser.parse_args()
    with args.data.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
    def col(n):return np.array([number(r.get(n)) for r in rows])
    y=col('IntrusionsTotal'); a=col('InterventionCondition'); assert np.isfinite(y).all() and np.isin(a,[0,1]).all()
    mood=np.nanmean(np.array([col('Mood'+k+'Pre') for k in ['Sadness','Depression','Hopelessness']]),axis=0)
    x=np.array([a,mood,col('PupilBaseline'),col('PupilRest')-col('PupilBaseline'),col('PupilMemoryReminderEffect'),col('PupilCognitiveTaskEffect')]).T
    groups={str(v):{'n':int((a==v).sum()),'mean':float(y[a==v].mean()),'median':float(np.median(y[a==v]))} for v in [0,1]}
    difference=groups['1']['mean']-groups['0']['mean']; rng=np.random.default_rng(20260908); n1=groups['1']['n']; ge=0
    for _ in range(10000):
        perm=rng.permutation(y); d=perm[:n1].mean()-perm[n1:].mean();ge+=abs(d)>=abs(difference)
    models={'treatment':[0],'treatment_mood':[0,1],'pre_task_pupils':[0,1,2,3,4],'during_task_pupil':[0,1,2,3,4,5]}; metrics={};predictions={};penalties={}
    for name,inds in models.items():
        xx=x[:,inds]; keep=np.isfinite(xx).any(axis=0); p,alpha=loo(xx[:,keep],y)
        metrics[name]={'mae':float(np.mean(np.abs(p-y))),'rmse':float(np.sqrt(np.mean((p-y)**2))),'globally_empty_columns_dropped':int((~keep).sum())};predictions[name]=p.tolist();penalties[name]=alpha
    two=x[:,[4,5]];mask=(a==1)&np.isfinite(two).all(axis=1);coef=np.linalg.lstsq(np.column_stack([np.ones(mask.sum()),two[mask]]),y[mask],rcond=None)[0]
    result={'source':'https://www.nature.com/articles/s41746-025-02145-5','data_url':'https://osf.io/download/8qhp7/','raw_sha256':hashlib.sha256(args.data.read_bytes()).hexdigest(),'analysis_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'n':len(y),'groups':groups,'intervention_minus_control_mean':difference,'permutation_p_two_sided':(ge+1)/10001,'permutations':10000,'metrics':metrics,'missing_features':{k:int((~np.isfinite(x[:,i])).sum()) for i,k in enumerate(['treatment','mood','pupil_baseline','pupil_rest_delta','pupil_reminder_delta','pupil_task_delta'])},'reported_association_check':{'n':int(mask.sum()),'intercept':float(coef[0]),'reminder_coefficient':float(coef[1]),'task_coefficient':float(coef[2]),'interpretation':'Exploratory post-treatment association, not a causal arousal target.'},'scope':'Reanalysis of published data, not new independent trial; randomized package contrast, no isolated AI effect, no tested physiological feedback policy. Model scales/physiology effects cannot be transported to IDA without validation.','predictions':predictions,'penalties':penalties}
    args.out.write_text(json.dumps(result,indent=2)); print(json.dumps({k:v for k,v in result.items() if k not in ['predictions','penalties']},indent=2))

if __name__=='__main__':main()
