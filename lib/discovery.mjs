// All scenario effect sizes are hypothetical, dimensionless assumptions.
export const defaultScenario={name:'Relief, capacity, and persistent drive',states:['Transient load','Persistent drive','Limited capacity','Observation offset'],prior:[.25,.25,.25,.25],actions:['No added input','Dampen the signal','Support capacity','Corrective update'],immediate:[[.55,.55,.55,.55],[.12,.12,.12,.12],[.38,.40,.30,.50],[.48,.42,.65,.50]],loss:[[.20,.80,.90,.20],[.18,.75,.85,.20],[.20,.65,.25,.20],[.18,.22,.95,.20]],costs:[0,.03,.08,.06],probes:[{name:'Observe return history',means:[.15,.60,.55,.50],cost:.01},{name:'Measure response to a small challenge',means:[.30,.40,.90,.30],cost:.035},{name:'Compare response across contexts',means:[.25,.85,.35,.25],cost:.04},{name:'Use an independent reference',means:[.55,.55,.55,.05],cost:.02}],assumption:'Each hypothesis has the same initial reading (0.55). The matrices posit different later outcomes and probe responses. This fixture illustrates experimental design; it is not a calibrated nervous-system model.'};
const bounded=x=>typeof x==='number'&&Number.isFinite(x)&&x>=0&&x<=1;
export function validateScenario(s){
 if(!s||typeof s.name!=='string'||!Array.isArray(s.states)||s.states.length<2||s.states.length>12) throw Error('Use 2–12 named hypotheses.');
 const n=s.states.length,m=s.actions?.length;
 if(!m||m<2||m>12||s.states.some(x=>typeof x!=='string')||s.actions.some(x=>typeof x!=='string')) throw Error('Use 2–12 named actions.');
 if(new Set(s.states).size!==n||new Set(s.actions).size!==m) throw Error('Names must be unique.');
 if(!Array.isArray(s.prior)||s.prior.length!==n||!s.prior.every(bounded)||Math.abs(s.prior.reduce((a,b)=>a+b,0)-1)>1e-8) throw Error('Prior probabilities must sum to one.');
 for(const f of ['loss','immediate']) if(!Array.isArray(s[f])||s[f].length!==m||s[f].some(r=>!Array.isArray(r)||r.length!==n||!r.every(bounded))) throw Error(f+' needs a bounded row per action and column per hypothesis.');
 if(!Array.isArray(s.costs)||s.costs.length!==m||!s.costs.every(bounded)) throw Error('Each action needs a cost between zero and one.');
 if(!Array.isArray(s.probes)||s.probes.length<1||s.probes.length>12||s.probes.some(p=>typeof p.name!=='string'||!bounded(p.cost)||!Array.isArray(p.means)||p.means.length!==n||!p.means.every(bounded))) throw Error('Each probe needs a name, cost, and bounded mean per hypothesis.');
 return {...s,assumption:typeof s.assumption==='string'?s.assumption:'User-supplied hypothetical scenario. Effects are unvalidated.'};
}
const dot=(a,b)=>a.reduce((t,v,i)=>t+v*b[i],0);
export function decide(s,prior=s.prior,threshold=.4){
 const scores=s.loss.map((r,i)=>({index:i,action:s.actions[i],expectedLoss:dot(r,prior),total:dot(r,prior)+s.costs[i],worstLoss:Math.max(...r.filter((_,j)=>prior[j]>1e-8)),acceptableStates:r.map((v,j)=>v<=threshold?s.states[j]:null).filter(Boolean)}));
 const best=scores.reduce((a,b)=>a.total<=b.total?a:b),robust=scores.filter(a=>a.worstLoss<=threshold);
 const perfectInformation=prior.reduce((t,p,j)=>t+p*Math.min(...s.loss.map((r,i)=>r[j]+s.costs[i])),0);
 return {scores,best,robust,perfectInformation,maxInformationValue:Math.max(0,best.total-perfectInformation)};
}
export function posterior(prior,means,observation,noise){
 if(!Number.isFinite(observation)||!Number.isFinite(noise)||noise<=0) throw Error('A finite observation and positive noise are required.');
 const logs=prior.map((p,i)=>p>0?Math.log(p)-.5*((observation-means[i])/noise)**2:-Infinity),max=Math.max(...logs),w=logs.map(v=>Math.exp(v-max)),total=w.reduce((a,b)=>a+b,0);
 return w.map(x=>x/total);
}
export function rankProbes(s,prior,noise=.12){
 const before=decide(s,prior).best.total;
 return s.probes.map((p,index)=>{const lo=Math.min(...p.means)-7*noise,hi=Math.max(...p.means)+7*noise,steps=600,dx=(hi-lo)/steps;let after=0,mass=0;
  for(let k=0;k<steps;k++){const y=lo+(k+.5)*dx,w=prior.reduce((v,q,j)=>v+q*Math.exp(-.5*((y-p.means[j])/noise)**2)/(noise*Math.sqrt(2*Math.PI)),0)*dx;mass+=w;after+=w*decide(s,posterior(prior,p.means,y,noise)).best.total;}
  after/=mass;return {index,name:p.name,cost:p.cost,expectedAfter:after,value:before-after,netValue:before-after-p.cost};
 }).sort((a,b)=>b.netValue-a.netValue);
}
export function checkRecordClaim(results,r){
 if(!r||!['lookup','compare'].includes(r.kind)) return {status:'out_of_scope',reason:'This checker supports numerical records only. Mechanisms, treatment efficacy, and universal claims need additional evidence.'};
 const metrics=results.nominal.metrics;
 if(!['mae','rmse'].includes(r.metric)||!Object.hasOwn(metrics,r.model)) return {status:'rejected',reason:'Unknown model or measure.'};
 const scope='Exploratory held-out prediction. This record check does not validate the analysis or establish a causal effect.';
 if(r.kind==='lookup') return {status:'record_supported',value:metrics[r.model][r.metric],unit:'tank units',n:results.nominal.n,scope};
 if(!Object.hasOwn(metrics,r.other)) return {status:'rejected',reason:'Unknown comparator.'};
 const a=metrics[r.model][r.metric],b=metrics[r.other][r.metric];
 return {status:'record_supported',candidate:r.model,comparator:r.other,metric:r.metric,candidateError:a,comparatorError:b,improvement:b-a,lowerError:a<b,unit:'tank units',n:results.nominal.n,scope};
}
export function validateExperiment(p){
 if(!p||typeof p.outcome!=='string'||!p.outcome.trim()||!['observational','randomized'].includes(p.design)) throw Error('Specify an outcome and valid design.');
 if(!Number.isFinite(p.forecast)||!Number.isFinite(p.featureEnd)||!Number.isFinite(p.outcomeStart)||p.featureEnd>p.forecast||p.outcomeStart<=p.forecast) throw Error('Features must end by decision time; the outcome must occur later.');
 if(!Array.isArray(p.actions)||!p.actions.length||p.actions.some(a=>typeof a!=='string'||!a.trim())) throw Error('Name the actions or exposures.');
 if(p.design==='randomized'&&p.actions.length<2) throw Error('A randomized comparison needs at least two actions.');
 return {...p,status:'draft_for_research_review',inference:p.design==='randomized'?'Assigned-treatment contrast, subject to randomization integrity, missingness, interference, and analysis assumptions.':'Prediction only; this design does not identify a best intervention.',required:['Independent participant/session holdout','Timing and signal-quality audit','History-informed comparator','Frozen target and analysis','Independent outcome after withdrawal','Consent and appropriate oversight before prospective participant work']};
}
