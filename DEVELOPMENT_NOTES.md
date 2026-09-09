# StateAtlas / IDA Discovery Lab

A research application for the Daniel John Murray programme. It joins a finite measurement-and-action simulator, two real-data analyses, a 41-version paper map, research-draft validation and finite numerical claim checks.

Version 0.2 adds a searchable neuroscience atlas (28 resources, 13 measurement families, 14 failure modes and 10 research routes) and the IDA R1 headband engineering baseline. Start with `research/atlas/NEUROSCIENCE_AND_ENGINEERING.md` and `engineering/HEADBAND_R1.md`. The engineering package includes a modular OEM-based architecture, connection worksheet, 28 requirements, a bill of materials, prototype OpenSCAD/STL/SVG geometry and an offline raw-packet decoder with synthetic tests. It is not a manufactured or physically validated device. GitHub handoff instructions are in `GITHUB_HANDOFF.md`.

This is a working research prototype, not a treatment, clinical prediction service, generative AI assistant or connected device. Simulation matrices contain invented dimensionless values. They are not calibrated to humans. No participant session or physiological intervention is delivered.

## Run

Requires Node >=22.13 and pnpm. The project was scaffolded with @openai/create-sites 0.3.0 and the shadcn add-on. Preserve pnpm-lock.yaml.

```sh
pnpm install
pnpm dev
pnpm build
node --test tests/discovery.test.mjs tests/atlas.test.mjs
python -m unittest discover -s engineering/software -p "test_*.py" -v
```

The Windows host used during development had an asynchronous realpath compatibility problem and pnpm workspace-store verification trouble. Dependencies were installed through pnpm. The same declared dev/build entry point was then run directly with `node node_modules/vinext/dist/cli.js dev` / `build`. A task-local synchronous-realpath fallback preserved normal filesystem permission checks. Native dependency build scripts blocked by pnpm were not enabled; installed prebuilt binaries supported the successful build. This workaround is not needed by the hosted application.

## Interface

- Discovery lab: choose synthetic truth, simulate observations, change measurement noise, compare expected information value, inspect the full action table, import/export a scenario.
- Real-data tests: inspect both analyses and export their recorded numerical results. Cohorts and outcomes remain separate.
- Programme map: search all 41 manuscript versions and the prediction register; inspect typed links.
- Evidence: selected primary sources, their role and the inference boundary.
- Experiment designer: export a draft with a validated temporal ordering and a declared inference contract. Validation does not constitute scientific or ethics approval.
- Claim checks: compare numerical records or test rejection of an unsupported treatment assertion.
- Development path: the steps and research gates between this prototype and an eventual instrument.

Imported scenarios remain in browser memory and are lost on reload unless exported. There is no database or upload endpoint. The private hosted Site restricts access through the platform. No patient data, API keys or hardware credentials are used.

## Model and inference

For state probabilities p(z), action loss L(a,z) and action cost c(a), the current choice minimizes Σ p(z)L(a,z)+c(a). A probe's expected value is the reduction in that minimum after integrating its possible observations; net value subtracts probe cost. Gaussian likelihoods use stated noise. Midpoint quadrature uses 600 points over a range extending seven standard deviations beyond the extreme means. The tests compare with the perfect-information bound and with deliberately uninformative probes.

The default hypothesis matrix is a decision-method fixture. It assumes known probe responses and action effects, independent measurements, and only a scalar cost for probing. It does not model probe-induced state changes, longitudinal learning, exact IDA multiscale dynamics, neuronal mechanisms or intervention safety. The action table separates assumed immediate readings from later loss. Its robust-action display conditions on states with posterior probability above 1e-8 and a user-chosen loss threshold; it is not a safety certification.

The record checker is a finite JavaScript adaptation of authority separation, not a port or independent proof of the entire Python epistemic kernel. A file checksum or supported record does not establish source truth, statistical validity or clinical efficacy. No model-size or coverage/cost benchmark was run.

## Research reproducibility

The `research/` directory contains Python analyses, protocols, aggregate results and data retrieval/provenance instructions. NumPy is required. Raw ANTIDOTE numerical data are retrieved from the authors' public OSF link and are not redistributed in this repository; OSF node metadata did not expose a license. PhysioNet files are under ODbL 1.0; retain their license and attribution if redistributing a derived database. The app uses computed results and source links. The supplied research papers remain the author's work; this repository includes catalogue metadata, not manuscript PDFs.

Source code for the original AI supplement carries Daniel John Murray's MIT license; it has not been copied into this application. Dependencies retain their own licenses. No blanket license is assigned here to all research material or third-party data.

## Verification and limitations

- Fifteen Node tests pass, including ten original decision tests and five atlas/engineering integrity tests.
- Thirteen Python packet and quality tests pass. Five synthetic signal/fault scenarios ran; no physical acquisition was tested.
- The prototype carrier's analytic mesh is closed and oriented with the expected volume. It was not fabricated or fit-tested.
- TypeScript check and production build pass.
- Both research analysis scripts ran locally; the secondary analysis reproduced the reported phase-specific coefficients.
- A local route returned HTTP 200. Broad browser interaction/visual QA was not requested and was not performed.
- Optional WebMCP tools are feature-detected. Runtime registration/invocation was not verified in a supported browser context; they are not required to use the interface.
- This is not a powered prospective clinical validation or independent replication of a treatment trial.

The app's optional tools are `read_ida_research_state`, `run_ida_simulated_probe`, and `check_ida_numerical_record`. They share the visible state and finite calculation functions. No tool applies a human intervention.

## Next development

Independent analysis review; prospective repeated-session measurement testing; an appropriately reviewed randomized fixed-versus-state-guided intervention experiment; independent outcomes after withdrawal; validated transition models; justified sensor selection; runtime isolation and external evidence binding. The related redox/cancer branch needs its own mechanisms, calibrated probes, target-cell objectives and laboratory validation.
