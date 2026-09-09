# Reproduce the empirical work

Python 3.12 and NumPy were used. No sklearn or scipy dependency is needed.

From the project directory:

```sh
python research/download_sources.py --destination local-data
python research/analyze.py --raw local-data/physionet --out local-results/physionet
python research/analyze_antidote.py --data local-data/antidote/data.csv --out local-results/antidote.json
```

Create `local-results` before the final command if the previous command was not run. Raw data and fresh outputs are intentionally ignored by Git. The downloader checks against the exact input hashes from this run and stops on a change instead of silently substituting a new version. Network access is needed only for retrieval.

Analysis 001 was specified locally before outcome fitting; its freeze hash is in protocol_freeze.json. Analysis 002 was specified after reading the published findings and data dictionary, before retrieving the numerical table. Neither is publicly preregistered or an independent confirmatory sample. The opposite phase coefficients in analysis 002 were already published.

The scripts use participant-held-out nested ridge regression with a fixed penalty grid. Secondary-analysis missingness handling occurs within training folds. The primary analysis uses a simple native/log coordinate deadband aggregate, not a validated neural coordinate or the complete multiscale IDA algorithm.

The raw PhysioNet data are by Roy and Nuamah, DOI 10.13026/x3vc-p627, version 1.0.0. Their ODbL 1.0 license is retained in PhysioNet_LICENSE.txt. The ANTIDOTE data are by deBettencourt et al., DOI 10.1038/s41746-025-02145-5, from https://osf.io/anvuk/. Its numerical table is fetched from the authors' source, not redistributed here. No license was exposed in the OSF node metadata inspected during this run.

The statistical code and results do not establish a best treatment, a clinical biomarker, or an isolated AI-guidance effect. Read IDA_Project_Position.md and the two protocols for endpoints, limitations and next experiments.
