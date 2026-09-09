# IDA / StateAtlas

**The experimental instrument of [The Empirical Architecture](https://github.com/thantiklermcirony/empirical-architecture).**

IDA investigates which measurements distinguish states that need different interventions, and whether using those distinctions improves later outcomes. StateAtlas makes that question explorable through a working research application.

## What you can use

- A finite discovery lab for comparing measurements, uncertainty and intervention choices.
- A searchable map of 41 manuscript records and the programme’s prediction register.
- Two recorded analyses of existing physiological data, with results and provenance.
- An experiment designer with explicit temporal ordering and inference contracts.
- A neuroscience atlas covering 28 resources, 13 measurement families, 14 failure modes and 10 research routes.
- The R1 instrument engineering baseline, including requirements, prototype geometry and a tested decoder for synthetic packets.

## Run locally

Requires Node 22.13 or newer and pnpm. Research analyses additionally require Python and NumPy.

```sh
git clone https://github.com/thantiklermcirony/ida-stateatlas.git
cd ida-stateatlas
pnpm install
pnpm dev
```

```sh
pnpm build
node --test tests/discovery.test.mjs tests/atlas.test.mjs
python -m unittest discover -s engineering/software -p "test_*.py" -v
```

## Explore the source

[Scientific and development notes](DEVELOPMENT_NOTES.md) · [Neuroscience and engineering atlas](research/atlas/NEUROSCIENCE_AND_ENGINEERING.md) · [R1 engineering baseline](engineering/HEADBAND_R1.md) · [Contributing](CONTRIBUTING.md) · [Licensing](LICENSING.md)

The native source is now directly browsable. The original version 0.2 source commit is `52937c5e9f2297d03f250986574dd813c9d22907`; the preserved project ZIP, Git bundle and original manifest retain that handoff and its two development commits. The current source adds the programme identity, public documentation and licensing. Private hosting configuration is excluded from the native publication tree.

## Research status

The application is a research prototype. Its simulation matrices are synthetic and dimensionless. The R1 design has not been fabricated or physically validated. The two existing-data analyses do not establish useful added predictive value for the selected physiological features. The next scientific step is to test whether additional state information improves an independently assessed later outcome against a strong fixed-intervention comparison.

The current application does not run a generative model or deliver a human intervention. The broader programme’s claims about AI economics, biological discovery and consciousness remain research questions with explicit tests.

## How IDA advances the programme

Predictive-state foundations specify which distinctions a model needs. Action and viability specify which distinctions can change a decision. IDA connects those foundations to measurements, experiments and instrument development. UHL supplies a conditional composition/geometry research line within the larger programme.

Founded by Daniel John Murray. Original code and documentation are available under the MIT License; third-party sources retain their own terms.
