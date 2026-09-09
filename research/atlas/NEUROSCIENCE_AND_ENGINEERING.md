# IDA neuroscience atlas and headband design baseline

8 September 2026 · Daniel John Murray research programme

**The strongest project is a causal response atlas: identify which accessible measurements distinguish states that benefit from different inputs, then test whether using those distinctions improves independent later outcomes.** The headband is one possible instrument for that project. Its sensor set should be determined by measured incremental value.

This release expands StateAtlas with a neuroscience data map and an engineering package. It is complete as a versioned design baseline, not as a field-wide systematic review, a manufactured headband or a validated treatment. Those distinctions matter because the remaining experiments determine the actual final product.

## What the evidence changes

The field already recognizes many problems that motivate IDA. Circular analysis, physiological artifacts and unstable population associations have established methods literature. RDoC already treats psychiatric research dimensionally. Closed-loop and state-dependent experiments already exist. IDA cannot claim these ideas merely because it describes them in a common language; it needs to improve representation, experimental efficiency or intervention outcomes relative to existing approaches.

The important opening is the gap between observing a state and choosing an action. A classifier can identify the task, fatigue, a diagnostic category or a future poor outcome while offering no information about which available intervention is better. A response atlas must record a pre-decision state, the assigned input, timing, independent later outcome and enough context to test transfer. Without that structure, more cross-correlation can multiply associations while leaving action selection unidentified.

There is no general guarantee of a perfect intervention. If two underlying states produce identical accessible observations but require conflicting actions, no classifier using those observations can always choose correctly. If every available input has a bad outcome in a state, improved measurement cannot create an effective input. Conversely, if the same action works across all relevant states, detailed state reconstruction may be unnecessary. These are finite decision-theoretic constraints, not pessimistic forecasts about IDA.

## Data map

The catalogue contains 28 resources across 13 measurement families. Each record specifies usual use, access status, an IDA test and a limit on inference. Only the two previously reported IDA datasets have completed numerical reanalyses in this project. The others are candidate resources and documentation reviews; their raw files were not all downloaded or audited.

| Resource | Measurements / design | IDA use | Main boundary |
|---|---|---|---|
| [OpenNeuro](https://docs.openneuro.org/user-guide/) | EEG / MEG / MRI / iEEG; BIDS repository | Select repeated sessions with raw signals, events and independent later outcomes. | A repository is not one harmonized experiment. Check every dataset license and protocol. |
| [NEMAR](https://nemar.org/) | EEG / MEG / iEEG; Electrophysiology discovery portal | Find candidate EEG datasets and quality information. | Overlaps OpenNeuro; do not count duplicates as replication. |
| [HCP Young Adult](https://www.humanconnectome.org/study/hcp-young-adult) | MRI / diffusion / MEG; Population and retest | Study reliability and paired-modality transfer questions. | Healthy cohort and scanner measurements do not establish wearable intervention targets. |
| [ABCD](https://abcdstudy.org/scientists/data-sharing/) | MRI / behaviour / development; Longitudinal cohort | Separate age/development, context and within-person change. | Current access is not an unrestricted NDA download; no minors’ data retrieved. |
| [UK Biobank](https://www.ukbiobank.ac.uk/use-our-data/) | Imaging / genetics / health; Population cohort | Test broad transport and confound hypotheses. | Population risk is not a moment-to-moment control policy. |
| [Sleep-EDF Expanded](https://physionet.org/content/sleep-edfx/1.0.0/) | EEG / EOG / EMG / sleep; Annotated longitudinal signals | Benchmark state transitions, signal quality and sparse-channel limitations. | Sleep-stage labels are not mental-health outcomes; verify montage and historical scoring. |
| [PhysioNet EEG Motor Movement/Imagery](https://physionet.org/content/eegmmidb/1.0.0/) | EEG / task events; Repeated task recordings | Test raw ingestion, artifact sensitivity and split integrity. | Task classification is not evidence of stabilization. |
| [CHB-MIT](https://physionet.org/content/chbmit/1.0.0/) | Clinical EEG / seizure labels; Clinical monitoring | Stress-test false-alarm burden and subject-held-out evaluation. | Paediatric epilepsy cannot calibrate an adult anxiety controller. |
| [Temple EEG corpora](https://isip.piconepress.com/projects/nedc/html/tuh_eeg/) | Clinical EEG / reports; Clinical archive and subcorpora | Challenge generalization to real clinical noise and devices. | Reports and clinical sampling introduce selection and label biases. |
| [WESAD](https://archive.ics.uci.edu/dataset/465/wesad+wearable+stress+and+affect+detection) | ECG / EDA / respiration / motion; Lab stress and affect | Compare physiology against context and task order. | Protocol labels can be decoded without identifying causal intervention response. |
| [DEAP](https://www.eecs.qmul.ac.uk/mmv/datasets/deap/) | EEG / peripheral / affect ratings; Stimulus and rating experiment | Candidate only after access and raw/preprocessed audit. | Processed signals and stimulus labels can erase recovery and treatment information. |
| [OMEGA](https://www.mcgill.ca/bic/neuroinformatics/omega) | MEG / anatomy; MEG archive | Evaluate neural-feature reliability before proposing scalp surrogates. | MEG features need an empirical transfer bridge to a headband. |
| [Cam-CAN](https://cam-can.mrc-cbu.cam.ac.uk/dataset/) | MEG / MRI / cognition; Lifespan multimodal cohort | Test age transport and stable versus dynamic features. | Between-person age associations do not describe within-person recovery. |
| [Healthy Brain Network](https://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/) | EEG / MRI / clinical / behaviour; Developmental clinical resource | Compare symptoms, context and multimodal representations. | Clinical ascertainment and development need explicit modelling. |
| [iEEG / HABITAT](https://www.ieeg.org/) | Intracranial EEG; Study-specific recordings | Find mechanistic timing evidence and perturbation studies. | Electrode coverage and clinical selection prevent direct scalp transport. |
| [DANDI](https://dandiarchive.org/) | Cellular / systems neurophysiology; NWB-oriented archive | Obtain perturbation-labelled mechanistic datasets. | Animal/cellular scale needs explicit bridges to human outcomes. |
| [International Brain Laboratory](https://www.internationalbrainlab.com/data) | Spikes / behaviour / task; Standardized multicentre experiments | Test history, latent-state and across-lab prediction. | Mouse task dynamics are not human clinical treatment rules. |
| [Allen Brain Map](https://brain-map.org/) | Cell types / anatomy / expression / physiology; Atlases and experiments | Constrain plausible mechanisms and measurement operators. | An atlas is not a personal real-time state estimate. |
| [MICrONS](https://www.microns-explorer.org/) | Electron microscopy / calcium; Matched structural and functional connectomics | Study how wiring constrains observables and dynamics. | Mouse visual cortex is neither whole-brain control nor a mental-health headband model. |
| [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/) | Gene expression / single-cell; Study archive | Generate molecular hypotheses with tissue/time context. | No shared participant keys or validated inference from scalp EEG to cellular redox. |
| [ADNI](https://adni.loni.usc.edu/data-samples/) | MRI / PET / biomarkers / cognition; Disease-progression cohort | Distinguish long-term capacity changes from short-term state. | Neurodegeneration models cannot be reused as universal mental-health models. |
| [PPMI](https://www.ppmi-info.org/access-data-specimens/guidance-resources) | Clinical / imaging / molecular / digital; Longitudinal Parkinson programme | Evaluate repeated measures and device transport questions. | Disease and intervention context must remain explicit. |
| [Natural Scenes Dataset](https://www.nature.com/articles/s41593-021-00962-x) | High-field fMRI / stimuli; Dense repeated visual experiment | Test representation sufficiency with known stimuli. | Visual reconstruction does not imply general mind reading or treatment selection. |
| [BNCI archive](https://bnci-horizon-2020.eu/database/data-sets) | EEG / BCI / task events; Benchmark collections | Compare sparse montages and timing under known tasks. | Interface control accuracy does not establish clinical benefit. |
| [Roy–Nuamah HCI resilience](https://physionet.org/content/neuro-stress-resilience-hci/1.0.0/) | HR / EDA / IBI / task performance; Stress–recovery–rechallenge | Existing IDA analysis tests later challenge forecasts. | Selected peripheral residue features did not earn inclusion. |
| [ANTIDOTE](https://www.nature.com/articles/s41746-025-02145-5) | Pupil / mood / assigned intervention / intrusions; Randomized experimental-trauma study | Reproduce effect; distinguish pre-decision and post-treatment information. | No isolated AI effect and no randomized pupil-guided delivery. |
| [EMBARC](https://www.nature.com/articles/s41587-019-0397-3) | EEG / depression / randomized treatment; Treatment-response study | Candidate for honest treatment-by-state interaction and policy-value tests. | A predictor can be prognostic without selecting the better treatment. |
| [Scangos PR01 / closed-loop depression](https://pmc.ncbi.nlm.nih.gov/articles/PMC8284979/) | Intracranial recordings / stimulation / symptoms; Personalized perturbation studies | Strong mechanistic precedent for individualized response mapping. | Single-person invasive evidence does not validate noninvasive sensors or inputs. |

## What can go wrong—and the repair

These are source-supported failure modes and stated research hypotheses, not a claim that all neuroscience is wrong. The implementation makes them testable requirements.

**F01 · Selecting and testing on the same data** (Documented failure mode). Feature, channel, window or subgroup selection can inflate the reported effect. [Circular analysis and double dipping](https://pmc.ncbi.nlm.nih.gov/articles/PMC2841687/)

Repair: Nest every fitted choice; freeze a final external test. Acceptance: No shared person, session or overlapping segment across the claimed test boundary.

**F02 · Motion becomes a brain network** (Documented failure mode). Motion can generate systematic functional-connectivity patterns. [Spurious functional connectivity from motion](https://www.sciencedirect.com/science/article/pii/S1053811911011815)

Repair: Keep motion and censoring records; test motion-only and matched-quality baselines. Acceptance: Effect must survive prespecified quality sensitivity analyses.

**F03 · Muscle activity becomes high-frequency EEG** (Documented failure mode). Scalp high-frequency activity can contain substantial muscle contributions. [Scalp EEG during paralysis and muscle contamination](https://pubmed.ncbi.nlm.nih.gov/17574912/)

Repair: Record EOG, movement and jaw/forehead artifact checks; retain raw signals. Acceptance: Candidate must add value beyond artifact channels.

**F04 · Band power is equated with one oscillator** (Documented failure mode). Aperiodic changes can alter power in a conventional band. [Periodic and aperiodic spectral parameterization](https://www.nature.com/articles/s41593-020-00744-x)

Repair: Compare periodic/aperiodic models; do not name a neurotransmitter from a band ratio. Acceptance: Report the decomposition and sensitivity to fit choices.

**F05 · Small associations become personal predictions** (Documented failure mode). Small population associations can be unstable under resampling. [Sample size and brain-wide associations](https://www.nature.com/articles/s41586-022-04492-9)

Repair: Match sample-size design to the estimand; report uncertainty and external performance. Acceptance: Do not claim every experiment needs thousands; repeated-person experiments are different designs.

**F06 · Pupil size becomes a unique transmitter meter** (Unsupported inverse inference). Pupil covariation is not a unique assay of one transmitter or circuit. [Pupil fluctuations and cortical neuromodulatory activity](https://www.nature.com/articles/ncomms13289)

Repair: Measure luminance, gaze, blink, task and medication context. Acceptance: Separate human proxy validation from animal mechanistic support.

**F07 · Scalp blood flow becomes cortical fNIRS** (Documented confounding risk). Systemic and superficial physiology can contaminate hemodynamic signals. [Best practices for fNIRS](https://pmc.ncbi.nlm.nih.gov/articles/PMC7793571/)

Repair: Include depth-sensitive controls and physiological regressors. Acceptance: A compact optical sensor needs demonstrated cortical sensitivity.

**F08 · Training a signal is assumed to treat symptoms** (Clinical inference gap). A credible matched control is needed to isolate feedback-specific benefit. [Double-blind placebo-controlled neurofeedback trial in ADHD](https://pubmed.ncbi.nlm.nih.gov/32853703/)

Repair: Measure independent symptoms/function and blind assessment where feasible. Acceptance: Learning the target is an intermediate outcome, not sufficient clinical success.

**F09 · Post-treatment physiology selects the earlier treatment** (Temporal/causal inference error). A measurement caused by treatment was unavailable at the earlier choice. [ANTIDOTE randomized experimental-trauma study](https://www.nature.com/articles/s41746-025-02145-5)

Repair: Time-stamp decision, feature cutoff, action and later outcome separately. Acceptance: Use it only for a later sequential decision in a valid design.

**F10 · Prediction is substituted for treatment selection** (Decision-design gap). A variable can predict poor outcomes under every action. [EEG prediction of antidepressant response](https://www.nature.com/articles/s41587-019-0397-3)

Repair: Estimate and validate treatment contrasts or policy value, not only outcome MAE. Acceptance: Beat the best fixed action with comparable burden.

**F11 · Clock alignment is assumed from a streaming library** (Engineering failure mode). Transport timestamps do not remove all sensor, buffering and stimulus latency. [Lab Streaming Layer time synchronization](https://labstreaminglayer.readthedocs.io/info/time_synchronization.html)

Repair: Retain raw counters and offsets; test physical marker latency. Acceptance: State measured timing uncertainty at the relevant decision horizon.

**F12 · Diagnostic categories are treated as one mechanism** (Framework limitation, already recognized in the field). Clinical categories need not imply a single physiological cause. [NIMH RDoC domains and constructs](https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc/definitions-of-the-rdoc-domains-and-constructs)

Repair: Use dimensions and competing mechanisms while retaining clinical outcomes. Acceptance: IDA must outperform existing dimensional and history-based models.

**F13 · A mouse or implanted-electrode effect is transported to a headband** (Unvalidated transport assumption). Species, sampling geometry and available interventions change. [State-dependent intracranial responses in depression](https://pmc.ncbi.nlm.nih.gov/articles/PMC8284979/)

Repair: Require a paired measurement bridge and a separate noninvasive intervention test. Acceptance: Conceptual similarity cannot substitute for a transport experiment.

**F14 · A resting atlas is treated as a controller** (IDA research hypothesis). Control needs action-conditioned transitions and later consequences. [Micro-randomized trials for adaptive interventions](https://pmc.ncbi.nlm.nih.gov/articles/PMC4732571/)

Repair: Collect repeated decision opportunities with assigned actions where justified. Acceptance: Demonstrate incremental policy value and generalization after withdrawal.

## Promising routes, ranked by usefulness for the next experiment

The ranking is qualitative. No defensible numerical probability of “solving the mind” can be calculated from these sources. A successful indication would be consequential without establishing one treatment for every mental-health problem.

**P01 · State-guided timing of an established behavioural input — First IDA priority.** An existing input can have measurable effects; physiological guidance still needs its own contrast. [ANTIDOTE randomized experimental-trauma study](https://www.nature.com/articles/s41746-025-02145-5)

Next: Same input/content budget: fixed versus state-guided versus matched control. Boundary: No benefit over fixed delivery after withdrawal stops the personalization claim.

**P02 · EEG added to context, behaviour and peripheral physiology — First measurement priority.** Scalp measurements can carry outcome information in defined settings. [EEG prediction of antidepressant response](https://www.nature.com/articles/s41587-019-0397-3)

Next: Incremental value, repeatability and treatment interaction in held-out sessions. Boundary: If simpler channels match performance, remove EEG from that use case.

**P03 · Respiration / HRV biofeedback with independent outcomes — Accessible intervention candidate.** There is randomized evidence in specific populations; transfer is unresolved. [Heart-rate variability biofeedback in substance-use treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489796/)

Next: Match instruction, attention and exposure; test the value of feedback timing. Boundary: A better HRV trace alone is insufficient.

**P04 · Cue- and phase-specific updating — Mechanistic priority.** Opposite phase associations motivate temporal distinctions, not causal prescriptions. [ANTIDOTE randomized experimental-trauma study](https://www.nature.com/articles/s41746-025-02145-5)

Next: Sequential design with pre-decision variables and later intrusive-memory or function outcomes. Boundary: Do not infer a universal arousal optimum.

**P05 · Closed-loop sleep research — Technically tractable separate branch.** EEG-timed sensory input has controlled experimental precedents. [Auditory closed-loop slow-oscillation stimulation](https://www.nature.com/articles/s41467-017-02170-3)

Next: Verify phase timing, arousal burden and independent next-day outcomes. Boundary: No transfer to awake psychiatric treatment without separate evidence.

**P06 · Personalized invasive mapping — Mechanistic precedent; specialist branch.** Individualized recording and stimulation can support clinical improvement in selected cases. [Closed-loop neuromodulation in an individual with depression](https://www.nature.com/articles/s41591-021-01480-w)

Next: Use published evidence to constrain hypotheses; require a scalp bridge. Boundary: No invasive stimulation implementation in the headband.

**P07 · State-dependent cognitive-control intervention — Mechanistic precedent; specialist branch.** An invasive proof-of-concept compared closed- and open-loop behavioural effects. [Closed-loop enhancement of cognitive control](https://www.nature.com/articles/s41551-021-00804-y)

Next: Test whether noninvasive measurements and permitted inputs preserve useful distinctions. Boundary: An implanted result cannot specify scalp stimulation parameters.

**P08 · tVNS and baseline-response interactions — Watch list; medical-device branch.** An emerging randomized study makes response heterogeneity a testable question. [MODULATE Depression and baseline HRV](https://www.nature.com/articles/s41398-025-03780-y)

Next: Independent confirmation of interaction and clinically reviewed device protocol. Boundary: No stimulation circuit or dosing in IDA R1.

**P09 · EEG neurofeedback for mental-health benefit — Conditional, mixed evidence.** Specific feedback effects require credible sham or active controls. [Double-blind placebo-controlled neurofeedback trial in ADHD](https://pubmed.ncbi.nlm.nih.gov/32853703/)

Next: Independent blinded outcome and adverse-burden comparison. Boundary: Changing a band ratio cannot be counted as symptom resolution.

**P10 · Neural mechanisms linked to redox / cancer — Separate mechanistic programme.** Molecular datasets can constrain biology at tissue/cell scales. [NCBI GEO](https://www.ncbi.nlm.nih.gov/geo/)

Next: Paired measurements, defined cell types and independent causal perturbations. Boundary: Scalp signals cannot currently determine tumour redox or cancer intervention.

## The chosen engineering route

R1 combines an existing eight-channel acquisition module with six proposed EEG channels, two EOG channels, a separate reference and bias, an adjustable harness, lead retention and the original enclosed electronics. A prototype carrier is specified in parametric CAD and a closed STL mesh. The physical electrode interface uses commercial contacts. The package includes the logical connection assignment, configuration contract, bill of materials, 28 requirements, an offline raw-packet decoder and synthetic bench fixtures.

Keeping the acquisition electronics and firmware from a documented supplier gives us actual upstream design resources. It does not waive board-revision checks, electrical-safety review, physical testing or intended-use validation. This release makes no custom-PCB manufacturing claim. The default carrier dimensions assume a case envelope and need to be changed after measuring the purchased unit.

The executable software decodes recorded packets, preserves raw counts/configuration, converts scales and reports quality/continuity problems. Thirteen tests passed. Five synthetic fault cases were run. The CAD mesh is closed and consistently oriented with the expected analytic volume. No real headband, live driver, human fit or clinical experiment was tested. An OEM recording workflow supplies real binary input; a text export is not interchangeable with raw packets.

The first development target is a useful research instrument, followed by validated measurement value, followed by validated state-guided intervention value. That sequence can lead to a smaller final headband, a peripheral-only tool, or a result that a headband does not help the selected indication. Each is informative.

## Next decisive experiment

Choose one defined population, independent later outcome and clinically justified input. Measure context and recent behaviour first, then peripheral channels, then EEG. Compare each increment on untouched sessions/people appropriate to the intended deployment. Require robust artifact and timing controls. Pre-decision features must precede the decision; later pupil/EEG changes cannot retrospectively select an earlier action.

If measurement value is established, compare fixed delivery against state-guided delivery with comparable content, exposure and attention. Include participant choice, burden and dropout in outcomes. Determine whether benefits survive input withdrawal and transfer across sessions. Treat state-by-treatment interactions and policy value as separate estimands from prognostic accuracy. Use a reviewed randomization scheme and a simulation-based sample-size plan based on plausible effects and repeated-measure structure—not an invented certainty from the current small studies.

## Completion and handoff

The site contains the searchable atlas, methodological problem register, intervention routes, engineering requirements, drawings and downloads. The project includes source code, protocols, test fixtures, CAD and reproducibility instructions. It is prepared for a GitHub repository; ownership and visibility have not yet been selected. No repository has been created, no components ordered and no collaborators contacted.

The map is broad but not exhaustive. Dataset-level licenses and raw-data audits, full-text risk-of-bias assessment, comprehensive trial-registry searches, and dedicated reviews of speech/social neuroscience, pain, autonomic disorders, development and medication interactions remain open. A final physical product still requires the actual hardware and verification programme. These are explicit unresolved tasks, not completed claims.
