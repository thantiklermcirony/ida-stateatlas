import {test} from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync,existsSync} from 'node:fs';
const read=p=>JSON.parse(readFileSync(new URL('../'+p,import.meta.url),'utf8'));
const atlas=read('data/neuro_atlas.json'),hardware=read('data/headband.json');
test('every dataset, failure and intervention route resolves to a source',()=>{
 const ids=new Set(atlas.sources.map(s=>s.id));assert.equal(ids.size,atlas.sources.length);
 for(const record of [...atlas.datasets,...atlas.failures,...atlas.routes])assert.ok(ids.has(record.source),record.id);
 for(const s of atlas.sources)assert.equal(new URL(s.url).protocol,'https:');
});
test('catalogue does not present unanalysed datasets as numeric validation',()=>{
 assert.equal(atlas.datasets.filter(d=>d.audit.startsWith('Numerical')).length,2);
 for(const d of atlas.datasets)for(const key of ['access','ida_test','limit','audit'])assert.ok(d[key].trim(),d.id+' '+key);
 assert.ok(atlas.open_coverage.length>=4);
});
test('hardware requirements link to a declared failure and distinguish physical work',()=>{
 const ids=new Set(atlas.failures.map(f=>f.id));
 for(const r of hardware.requirements)assert.ok(ids.has(r.failure),r.id);
 assert.ok(hardware.requirements.some(r=>r.id==='R24'&&r.status==='Not established'));
 assert.ok(hardware.requirements.some(r=>r.id==='R08'&&r.status==='Not run'));
});
test('fixture data rate and quality claims match saved engineering results',()=>{
 assert.equal(hardware.bench.calculations.bytes_per_second,33*250);
 assert.equal(hardware.bench.cases.clean.usable_windows,3);
 assert.equal(hardware.bench.cases.flat.usable_windows,0);
 assert.equal(hardware.bench.cases.rail.usable_windows,0);
 assert.equal(hardware.bench.cases.dropout.continuity_issues,1);
});
test('engineering downloads exist and the copied atlas is identical',()=>{
 for(const name of ['carrier.svg','carrier.scad','carrier.stl','ida-r1-package.zip'])assert.ok(existsSync(new URL('../public/engineering/'+name,import.meta.url)));
 assert.deepEqual(atlas,read('research/atlas/neuro_atlas.json'));
 assert.equal(hardware.mesh.closed_oriented_edges,true);
 assert.equal(hardware.mesh.volume_mm3,hardware.mesh.expected_volume_mm3);
});
