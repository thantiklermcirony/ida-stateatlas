# IDA: a programme for discovering when and how an intervention can work

Prepared 8 September 2026 for Daniel John Murray. The accompanying application is an executable research workbench. It is not a validated treatment or a completed model of the mind.

**My choice is IDA, developed as a state-dependent intervention discovery system.** Its central experiment is to determine whether a feasible measurement can distinguish apparently similar states that benefit from different inputs or timing—and whether using that distinction produces a lasting improvement over an effective fixed intervention. The AI architecture supplies an evidence and authority layer. The redox/cancer work supplies a parallel experimental branch with its own mechanisms and desired outcomes.

This is substantially larger than building a stress detector or a headband. The instrument is the eventual embodiment of a successful measurement-and-action model. Its sensors, inputs and enclosure should change as that model earns or loses support.

## The scientific position

The programme's strongest common idea is that a convenient observation can erase distinctions that matter to a future. More accurate estimation of that same observation cannot necessarily recover the lost distinction. The resulting task is experimental: specify the future, construct competing explanations, choose discriminating measurements, and test whether they change a useful decision.

For mental health, a particularly consequential distinction is among **current relief, ability to withstand later demand, and a durable change in a cue-linked response**. These need not move together. Reducing a signal during an intervention might mask ongoing vulnerability. Conversely, useful engagement during a corrective task might temporarily increase an arousal-related measurement. A universal instruction to minimize arousal could therefore be the wrong objective.

Your eye-muscle analogy suggests an important question: which accessible input releases unnecessary regulatory effort? It is a productive search question. It does not establish that there is one corresponding switch for every nervous-system difficulty. We need to discover the accessible inputs, their state dependence, and the later consequences rather than assign those properties to an attractive analogy.

The most promising first target is a **state-and-phase map of intervention response**: when a system benefits from reduced demand, when it benefits from a restorative input, and when a different form of engagement changes the subsequent response. Those are research categories, not diagnoses or instructions to a patient.

Existing studies make this search credible. Personalized intracranial mapping has supported sustained improvement in one person with depression, while leaving generalization open. [Scangos et al.](https://www.nature.com/articles/s41591-021-01480-w) A randomized biofeedback study connected an accessible physiological intervention with later behavioral outcomes. [Eddie et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC12489796/) These precedents support asking the question; they do not establish IDA's specific controller or a universal nervous-system language.

## What I actually tested

I ran two distinct analyses. They do not share participants, outcomes, units or fitted coefficients.

**Analysis 001: recovery before a renewed challenge.** The open Roy–Nuamah data provided repeated task phases and peripheral physiology. [Dataset](https://physionet.org/content/neuro-stress-resilience-hci/1.0.0/) I downloaded 179 small files, totaling approximately 4.1 MB. All 178 files listed in the publisher's checksum table matched; the checksum table itself has no self-entry.

The locally fixed specification used the first recovery period to forecast second-stress task error. Thirty-four participants passed the timing and coverage rules; p02 had two event tags and was excluded without choosing one retrospectively. All models used nested leave-one-participant-out ridge regression, with scaling inside the training folds. This is exploratory cross-validation on one cohort, not a sealed external test.

| Model | Mean absolute error | Root mean squared error |
|---|---:|---:|
| Performance baseline | 191.15 | 249.57 |
| Add behavioral recovery history | 178.07 | 227.21 |
| Behavioral history plus current HR/EDA | 185.75 | 229.80 |
| Add HR/EDA residue to that comparator | 188.16 | 235.59 |

Lower is better; units are tank deviation. The selected residue features did not improve the primary comparison. The behavioral-history improvement was 6.8%, but its descriptive resampling interval included no benefit. Shifting physiological alignment by ±10 seconds did not reverse the primary result. The bootstrap resampled fixed out-of-fold errors; overlapping training folds mean it is not a confirmatory confidence procedure.

This was a simple IDA-inspired deadband aggregate. It did **not** test the full published leaky multiscale engine, addressed updating, EEG, clinical symptoms or a feedback intervention. Its practical conclusion is narrow: these two physiological features do not earn inclusion from this dataset and analysis. It is neither a validation nor a refutation of the entire programme.

**Analysis 002: an existing intervention and its physiological correlates.** I downloaded the numerical table for the published ANTIDOTE experiment and reproduced selected results. [Original study and data](https://www.nature.com/articles/s41746-025-02145-5) The assigned intervention group averaged 11.62 intrusive memories versus 21.00 in the active control group, with 50 participants per arm; a fresh 10,000-permutation test gave two-sided p≈0.0149. This is a reanalysis of an existing result, not a newly discovered treatment effect.

The reported intervention-arm two-predictor regression was reproduced: the reminder-phase coefficient was +33.21 and the subsequent task coefficient −28.41, with 45 complete cases. These are post-treatment associations. They do not identify causal arousal targets or establish that changing a pupil measurement would change the outcome.

In the separate person-held-out screen, mean absolute errors were 12.29 for treatment assignment, 12.44 after prior mood, 12.30 with pre-task pupil measures, and 12.36 after adding the during-task pupil measure. There was no clear useful gain from the selected physiological predictors. The during-task feature is unavailable for an earlier treatment-choice decision, so it cannot justify such a controller. Missing features were imputed inside training folds, with missingness indicators.

The important conjunction is **an intervention can work while a plausible monitoring feature has not yet earned its place in a personalized policy**. Both groups received AI guidance, and the study did not randomize pupil-guided delivery. Those distinctions define the next experiment.

## What the programme contributes to the next experiment

| Programme component | Development consequence |
|---|---|
| Biological State Sufficiency and Predictive Closure | Choose a declared future and challenge the adequacy of the present representation. |
| Viable Action | Look for distinctions that change acceptable actions; finer diagnosis is unnecessary when one action works across all relevant states. |
| IDA's return and frozen-reference construction | Compare trajectories and later outcomes without redefining improvement by moving the reference. |
| Addressed updating hypothesis | Test cue/context and phase separately; relaxation and corrective change must not be treated as identical. |
| Temporal Architecture | Preserve ordering, waiting and withdrawal, not just total exposure. |
| Redox plant/sensor/controller distinctions | Construct competing failure mechanisms and role-specific probes in the appropriate biological system. |
| Hormesis and control transmission | An induced response is not automatically a useful or durable functional gain. |
| Epistemic Type Safety | Keep records, hypotheses, simulations, causal conclusions and permitted actions separate. |

The application includes all 41 active manuscript-version entries and the earlier prediction-family register. Its cross-domain links are explicitly typed as logical dependencies, hypotheses, methods or analogies. This is a conceptual integration, not a pooled cross-correlation of incompatible biological datasets or an independent proof audit of all papers.

## The project built now

**StateAtlas / IDA Discovery Lab v0.1** contains:

- An executable finite hypothesis-and-action model with explicit scenario import/export, Bayesian belief updates and a reproducible synthetic observation record.
- Probe ranking by expected improvement in the next decision minus measurement cost, with a perfect-information bound.
- An action-by-state atlas separating immediate readings from assumed later outcomes after input withdrawal.
- Both numerical analyses, their actual outcomes, comparators and limitations.
- The searchable corpus, prediction dependencies and a selected primary-source evidence map.
- A research-draft builder that checks temporal ordering and distinguishes observational prediction from an assigned-treatment contrast.
- A finite record checker that reports numerical support while rejecting out-of-scope clinical assertions.

The model's effect sizes are **invented dimensionless fixtures**, visibly labeled as such. They test the method's operation and failure modes. They are not estimates of brain physiology or evidence of IDA efficacy. The Gaussian probes assume known likelihoods and independent observations, and price perturbation only through an assigned cost. Real active probes can alter the state and require a validated transition model. The model is a one-step decision experiment, not a recursive biological controller.

Ten automated tests cover informative and uninformative probes, perfect-information bounds, conflicting actions, a common best action, probability normalization, invalid scenarios, temporal leakage, scope rejection and programme references. TypeScript validation and the production application build passed. The existing Python AI supplement was also rerun: 34 checks, 18 valid numerical certificates, 10,000 restricted mutants with no false acceptance, and 2,401 finite action families. These finite checks do not prove general security or test the model-size hypotheses.

No clinical decision, trauma-exposure session, physiological actuation or device connection is implemented. There is no generative-model backend. The current authority component is a small record-checking demonstration; deployment isolation and broader evidence binding remain engineering work.

## The next complete experimental programme

**1. Establish measurement value.** Use existing datasets to compare frozen recovery features, generic time-history models and mechanistic alternatives. Acquire or collaborate on repeated-session data for the same people; the current small cohorts do not establish within-person readiness monitoring over time. Use independent symptom/function outcomes, rather than predicting the score the instrument itself defines.

**2. Establish state-dependent response.** Choose one clinically and experimentally justified input, then compare fixed delivery with state-guided delivery and an appropriate matched control. Hold the intervention content and exposure budget comparable. The target is the incremental value of the state estimate. Randomize timing or decision opportunities when feasible; do not infer the best action merely from correlations among arousal, engagement and outcome. Micro-randomized trials supply an established design route. [Klasnja et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4732571/)

**3. Test the phase distinction.** Declare whether the proposed state indicates a need for reduced demand, restored capacity, or a different opportunity for updating. Pre-action variables may inform selection; post-action engagement can inform a subsequent decision only if that sequential design and its causal assumptions are specified. Compare the proposed gating feature with ordinary context, recent behavior, expectancy and adherence measures.

**4. Test withdrawal and transfer.** Assess whether improvement persists after the input stops, whether it survives the declared rechallenge, and whether it generalizes across sessions or relevant contexts. Track symptom/function outcomes and burden together. Improvements confined to the actuator-on signal are not durable stabilization.

**5. Choose the instrument.** Start with synchronized task/context records and independently timed outcomes. Candidate channels include ECG/PPG with respiration and motion quality, EDA, and pupil responses with luminance controls. EEG is a candidate when a neural measurement resolves an action-relevant uncertainty that simpler channels cannot. This is a measurement comparison, not a hardware purchase recommendation. A headband becomes justified by demonstrated incremental value, feasible latency, repeatability and acceptable burden.

**6. Build the recursive controller only after those links hold.** It must retain enough history to update its state after an action and observation; detect missing data and distribution change; respect input availability and participant choice; log every decision; and fall back to the reviewed protocol when its inference is unsupported. The finite action atlas does not itself provide these guarantees.

The first research team needs expertise in the chosen mental-health target, psychophysiology, causal/sequential trial design and software instrumentation. A later device collaborator needs a tested sensor/actuator requirement, not a speculative enclosure. These are roles for collaboration; nobody has been contacted.

## Where cancer fits

The redox branch offers a separate route to test whether matched present readings conceal different regenerative capacity and different rescue opportunities. It needs independently calibrated measurements of supply, demand and control response, then role-specific perturbations and later outcomes. It must not borrow neural sensor interpretations or human coefficients.

For cancer, the objective is also different: a useful result may be loss of tumour clonogenic survival while preserving normal tissue. Maximizing recovery indiscriminately is not the goal. A shared workbench can express those competing outcomes, costs and timing constraints, while each biological model remains independently accountable to its data.

The general discovery would be a transferable **experimental method** for finding actionable state, not a claim that cancer, mental illness and AI have the same physical mechanism.

## What would change my position

The decisive positive result is a whole chain: similar readings conceal different intervention requirements; a feasible measurement distinguishes them before the opportunity closes; a state-guided policy beats a strong fixed or history-informed policy; and its benefit persists on an independent endpoint. That would justify substantial investment and a concrete instrument programme.

A feature that loses to ordinary history should be retired or revised openly. An effective fixed intervention with no additional personalization benefit may still be valuable, but it does not validate the proposed state-guided mechanism. A model whose states cannot be separated by accessible probes does not justify manufacturing certainty.

Better measurement does not logically guarantee a perfect intervention: the available inputs may not control the relevant state, useful distinctions may be inaccessible in time, goals may conflict, or some damage may not be reversible. Making these limits explicit strengthens the project because the engine can reveal precisely which new measurement, actuator or experiment is needed.

The warranted position today is therefore ambitious and concrete: **we now have a working research platform and a specific missing experimental link to pursue. We do not yet have the final intervention.**
