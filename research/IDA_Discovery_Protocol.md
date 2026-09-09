# IDA discovery test 001 — recovery before renewed demand

7 September 2026. Local exploratory specification fixed before computing outcomes or fitting models. This is not a public preregistration or an independent confirmation.

Question: does recovery history improve prediction of the next challenge's task performance beyond observed ability, previous challenge performance, and the latest physiological snapshot?

Data: Roy and Nuamah, Neurophysiological Dataset of Stress Resilience During Human-Computer Interaction, version 1.0.0, DOI https://doi.org/10.13026/x3vc-p627. Initially use only MATB-II, HR, EDA, IBI, tags and metadata. Preserve original bytes and verify published hashes. Do not infer that recorded HR is beat-level HRV. The cohort has 35 participants; samples within a participant are not independent replications.

Forecast: immediately before Stress 2, nominal elapsed time 1080 seconds from Working Baseline start. Predict Overall Deviation (root mean squared deviation across both tanks) during Stress 2, 1080–1440 seconds. Lower values indicate better performance. Use half-open intervals; exclude exact boundary observations from the preceding phase. All features must precede the forecast, including preprocessing inputs. Align physiological data using the sole Working Baseline tag. If tags are missing or ambiguous, exclude the participant from physiology comparisons without reference to outcomes. All model comparisons use the same eligible participants.

Eligibility: at least 80% expected observations in each feature/target interval; monotonically increasing task times; finite values; at least 80% physiological coverage in baseline (0–360 s), recovery (720–1080 s), and latest minute (1020–1080 s). Nonpositive HR or negative EDA is invalid. Flat physiological signals are flagged, with exclusions decided by signal quality rather than target values. Do not drop valid extreme performance outcomes. Record discrepancies and any amendments explicitly.

Fixed model ladder, no outcome-based feature selection:

1. Training mean and persistence (Stress 1 OD) reference predictions.
2. Performance baseline: Working Baseline OD, Stress 1 OD, latest recovery-minute OD.
3. Snapshot: baseline plus latest-minute mean HR and log(1 + EDA).
4. Generic physiology history: snapshot plus recovery-mean HR and log(1 + EDA), each minus its Working Baseline mean.
5. Recovery residue: snapshot plus one feature per physiological channel: mean over Recovery 1 of max(abs(channel minus its Working Baseline mean) minus its Working Baseline standard deviation, 0). Normalize each by max(baseline standard deviation, 1 bpm for HR or 0.01 for log(1 + EDA)). This is an IDA-inspired candidate, not the complete published IDA algorithm or a demonstrated biological reserve measure.
6. Behavioral history: performance baseline plus OD during the first and middle two-minute thirds of Recovery 1. This checks whether inexpensive task history already supplies useful information.
7. Combined comparator: snapshot plus the two behavioral-history features, compared with the same model plus the two residue features. This is the demanding primary incremental-value comparison.

Use linear ridge regression. Standardize using training participants only. Choose penalty from [0.1, 1, 10, 100, 1000] by inner leave-one-participant-out mean squared error; outer leave-one-participant-out predictions assess performance. Intercept is unpenalized. No neural network, feature fishing or tuning after seeing the result. Report MAE and RMSE in tank units, all participant predictions, selected penalties, and the distribution of paired absolute-error differences. Bootstrap paired fixed out-of-fold errors for a descriptive stability interval only: overlapping training sets and small N prevent treating that interval as confirmatory inference.

Prespecified sensitivities: shift physiological alignment by -10 and +10 seconds; retain the nominal task target; report the full ladder without picking whichever alignment wins. Report results with and without individually identified technical signal failures. A benefit only against a weak snapshot comparator does not establish unique IDA value.

Interpretation: this can screen for useful measurement history. It cannot identify the best intervention, prove hidden physiological capacity, establish clinical readiness, or show within-person monitoring works over days. Positive results require independent repeated-session replication. Negative results reject this candidate on this dataset, not every possible IDA implementation. Intervention selection requires later randomized action variation and an outcome measured after feedback withdrawal.
