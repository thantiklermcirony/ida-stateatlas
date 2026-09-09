# StateAtlas / IDA Discovery Lab

Private source and history handoff for Daniel John Murray's research programme. Version 0.2.0, source commit `52937c5e9f2297d03f250986574dd813c9d22907`, originally prepared 8 September 2026 and preserved here 9 September 2026.

IDA asks which measurements distinguish states that need different interventions, and whether using those distinctions improves later outcomes. The current application includes the programme map, a finite measurement/action simulator, two real-data analyses, a neuroscience resource atlas and the R1 headband engineering baseline.

## Get the complete project

- [Source ZIP](StateAtlas_IDA_v0.2_Project.zip): all 130 source files, locked dependencies, research material and engineering files. Extract the `StateAtlas_IDA` directory.
- [Git history bundle](StateAtlas_IDA_v0.2.bundle): the complete existing Git history, including both development commits.
- [Manifest](MANIFEST.json): source revision, file hashes and verification record.

This initial GitHub handoff stores the source as an archive and a Git bundle. Application files are inside those downloads; the web repository does not yet expose the application source as individual files. A normal authenticated Git push can publish the preserved source history as a separate branch without replacing this handoff commit.

With Git installed, download the bundle and run:

```sh
git clone StateAtlas_IDA_v0.2.bundle ida-stateatlas-source
cd ida-stateatlas-source
```

The checked-out source includes its own detailed README and GitHub handoff guide. To add its existing history to this repository without a force-push:

```sh
git remote add github https://github.com/thantiklermcirony/ida-stateatlas.git
git push github main:source-v0.2
```

This command requires the owner's normal GitHub authentication. It creates a source branch; it does not merge with or overwrite the handoff branch.

## Run and verify

Requires Node >=22.13 and pnpm; research analyses additionally require Python/NumPy.

```sh
pnpm install
pnpm dev
pnpm build
node --test tests/discovery.test.mjs tests/atlas.test.mjs
python -m unittest discover -s engineering/software -p "test_*.py" -v
```

The 15 Node tests and 13 Python tests passed again during this handoff. Git bundle and ZIP integrity checks passed. The original task reported a successful TypeScript check and production build at the same source revision; those build checks were not repeated during the handoff.

## Current research position

The finite simulator uses invented dimensionless fixtures. The engineering baseline has not been fabricated, physically tested or clinically validated. The two analyses reproduce/explore existing data; the selected physiological features did not establish useful added predictive value. The next scientific target is a prospective comparison of an effective fixed intervention with state-guided selection or timing, using an independent later outcome.

The source contains aggregate research outputs and retrieval instructions, plus synthetic engineering fixtures. No raw participant dataset is included in this handoff. No new blanket licence has been assigned to the project; existing third-party terms and attributions remain in the source. Keep this repository private until publication scope and licensing have been chosen.

## Role in the wider programme

Predictive-state foundations define what needs to be distinguished. Viable-action work defines which distinctions change a decision. Epistemic type safety separates a proposal, a supported record and an authorized action. UHL composition models form a conditional mathematical branch; an observer-coupling hypothesis is not a prerequisite for this application.
