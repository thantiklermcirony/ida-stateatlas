# GitHub handoff

The source tree is ready for an owner-controlled GitHub repository. No GitHub repository has been created or published by this task. The owner account/organisation and visibility are awaiting selection. The existing private Sites source repository is a different service and must not be described as GitHub.

Suggested repository name: `ida-stateatlas`. Preserve the existing Git history. Push through the owner's normal authenticated GitHub workflow after choosing the destination. Do not embed credentials in remote URLs or committed files. Do not force-push an existing unrelated repository.

The repository includes:

- Application source and locked dependencies.
- Neuroscience catalogue, source register, limitations and next-test records.
- R1 headband design baseline, logical connections and engineering requirements.
- Prototype OpenSCAD/STL/SVG carrier, synthetic binary fixtures and parser tests.
- Earlier reproducible IDA data analyses, with raw data retrieval instructions.
- Contribution guidance and a research/engineering issue template.

No blanket public redistribution license has been selected for new project code, documentation and hardware. Select those deliberately before advertising the repository as open source. Dataset, manufacturer, dependency and manuscript terms remain separate. The original AI supplement's MIT license does not automatically license this entire project.

Checks from the repository root:

```sh
node --test tests/discovery.test.mjs tests/atlas.test.mjs
python -m unittest discover -s engineering/software -p "test_*.py" -v
python engineering/software/run_bench.py
pnpm build
```

Do not upload local raw participant data or runtime secrets. The engineering ZIP contains synthetic bench data only. Physical acquisition, fit, electrical safety, sensor value and intervention efficacy remain open requirements, not completed milestones.
