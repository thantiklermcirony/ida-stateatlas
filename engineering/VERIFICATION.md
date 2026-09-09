# Verification plan and release gates

R1 is a modular research acquisition design. The present evidence establishes software behaviour on synthetic packets. It does not establish performance on a physical Cyton, on people, or as a treatment. Preserve failures and raw data in the test record. Targets below are engineering proposals; they are not manufacturer guarantees or inferred clinical thresholds.

## Bench protocol

1. **Configuration audit.** Record supplier, serial number, board revision, battery/case revision, firmware startup text and register readback. Compare every channel's gain, input type and reference routing with the logical net worksheet. A drawing or saved GUI preset is not readback evidence.
2. **Electrical and enclosure review.** A qualified engineer checks the assembled recording configuration, battery/polarity protection, connectors, accessible conductive parts and interaction with all peripherals. Keep the supplied case. No person is connected during signal-source or bench-instrument tests. Human-connected charging or an unreviewed wired link is outside R1.
3. **Noise and frequency response.** Use a suitable calibrated biopotential phantom. Save raw data with inputs shorted through documented source impedance; measure RMS in the exact declared band. Repeat for all channels and battery states. Inject traceable amplitudes at 1, 10 and 30 Hz; report gain and phase, source tolerance and filtering. The supplied 10 Hz sine is only a software fixture.
4. **Common mode, imbalance and crosstalk.** On the bench, compare differential response with common-mode input at local line frequency. Repeat with a declared source-impedance imbalance. Excite one channel and measure others. Retain the circuit and calibrator configuration; no arbitrary line-voltage test is prescribed here.
5. **Radio and counter faults.** Record a continuous one-hour phantom session under normal host load and a separately declared interference/load condition. Report raw packet counts, observable counter discontinuities, session resets, partial bytes, host timing gaps and data-loss bounds. Do not call continuity perfect from modulo counters alone.
6. **Latency and synchronization.** Record the physical stimulus/marker using an appropriate isolated bench input or independent timing instrument. Repeat at least 100 events per tested host condition. Report p50/p95/max sensor-to-host, intended-to-physical-output and cross-device timing error separately. Validate causal filter/window delay. The seconds-scale target does not qualify phase-specific stimulation.
7. **Mechanical fit.** Measure the actual OEM enclosure and contacts. Revise carrier parameters before fabrication; check retention without obstructing switches or stressing leads. Inspect edge finish, deformation, cleaning and wear. Proposed 520–640 mm head-fit range and ≤150 g mass require measurement. PLA/PETG printing is not a biological-safety qualification.
8. **Supervised recording feasibility.** Only after the hardware review and an appropriate research protocol: measure usable-data fraction, repeat placement, ocular/motion contamination, comfort, skin response and independent timing. Outcomes and withdrawals are reported even if EEG quality is poor. Predefine exclusion rules; do not retain only people with convenient anatomy or hair characteristics.

## Research success must be a separate test

Use independent later outcomes and group test partitions by participant, family where applicable, site and chronological session as required by the intended use. Hyperparameters, artifact cutoffs, feature selection, imputation and normalization belong inside training folds. An offline noncausal filter cannot support a real-time claim. Leave a genuinely untouched external or prospective set for the final claim.

The comparator ladder is: context and behaviour → history → peripheral physiology → EEG → the proposed IDA representation. Test each increment with uncertainty, calibration and burden. For treatment selection, evaluate a declared policy against fixed delivery with matched content/exposure, not just prediction error. Fit prognostic and treatment-interaction components separately. Report positivity/support, missingness and sensitivity assumptions. High classification accuracy on laboratory condition labels is not proof of useful intervention selection.

For repeated decisions, randomization can identify proximal causal contrasts when its assumptions hold. Select a clinically justified target and reviewed input before sample-size planning. Use simulation across realistic effect sizes, within-person correlation, adherence and missingness; do not calculate a definitive enrolment number from the small existing IDA analyses. An independent statistician should freeze the final analysis before recruitment.

## Release gates

| Gate | Release evidence | Current state |
|---|---|---|
| G0: reproducible software | Unit tests, deterministic fixtures, hashes and source revision | Implemented and tested locally |
| G1: physical acquisition | Configuration audit and complete phantom/electrical/timing results | Not run; no hardware available |
| G2: usable measurement | Supervised repeated-session quality and fit data | Not run |
| G3: incremental measurement value | EEG/IDA beats declared simpler comparator on untouched data | Not established |
| G4: incremental policy value | State-guided delivery beats matched fixed delivery on later outcomes | Not established |
| G5: product release | Manufacturing verification, intended-use validation and jurisdiction-specific review | Not started |

G0 does not imply G1. G3 does not imply G4. A negative G3 result can be a successful engineering decision to remove EEG from that application.
