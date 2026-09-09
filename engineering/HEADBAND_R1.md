# IDA R1 headband: engineering design baseline

Revision 0.2, 8 September 2026. **Status: design and software bench baseline; not a manufactured, human-tested or medically cleared device.** This package specifies an assemblable research architecture using an existing acquisition module. It does not claim a completed custom PCB, fitted production enclosure or validated treatment controller.

## Purpose and selected architecture

R1 measures scalp potentials, eye artifacts and movement with synchronized context records. Its scientific job is to test whether neural measurements add useful information about a declared later outcome and, eventually, an assigned intervention response. Recording a plausible brain signal is only the first engineering requirement.

Use an unmodified OpenBCI Cyton eight-channel module, its supplied case, radio dongle, battery and supported firmware. Its published design files and firmware are linked in `upstream.json`; retain the actual purchased board revision and firmware identity. This selects a documented development platform, not a claim of medical certification. Do not fabricate an old upstream PCB simply because Gerbers exist; revision errors and substitutions need independent review. [Manufacturer specifications](https://docs.openbci.com/Cyton/CytonSpecs/)

The head-worn assembly is an adjustable circumferential textile band with removable electrode carriers, lead retention and an optional rear module carrier. For the first recordings, use the original enclosed module off the head if mass or motion makes the rear carrier unsuitable. The carrier CAD is a fit prototype with explicit assumed enclosure dimensions; measure the purchased case before printing a fit revision. Use commercial electrode contact surfaces; printed parts are structural carriers, not qualified skin-contact electrodes.

The R1 channel plan is **six referential EEG channels and two bipolar EOG channels**, all sampled together. Posterior contacts make an occipital alpha comparator possible; a forehead-only product could not be assumed to preserve it. Four external EOG contact leads are part of the harness. An external respiration/ECG reference is a separate optional synchronized device, not an invented extra Cyton channel. Pupil diameter needs a calibrated camera and luminance record; EOG is not a pupil-size sensor.

## Signal and system requirements

All numbers labelled targets are proposed acceptance criteria, not measured product performance.

| Item | R1 requirement | Status / verification |
|---|---|---|
| Acquisition | 8 channels at nominal 250 samples/s, signed 24-bit raw counts | Documented protocol; hardware capture still required |
| EEG montage | Fp1, Fp2, F7, F8, O1, O2, named reference M1 | Candidate placement; trained placement and repeatability study required |
| Artifact channels | Vertical and horizontal bipolar EOG, independent of the common EEG reference | Candidate wiring; verify register routing and polarity on a signal phantom |
| Reference and bias | Distinct labelled contacts; bias is not protective earth | Manufacturer routing must be preserved |
| Scales | Store per-channel gain and reference voltage; convert counts using the recorded configuration | Implemented conversion fixture; calibrate actual unit |
| Useful research band | Proposed 0.5–40 Hz analysis branch, raw stream retained | Not suitable for claims about DC shifts or high-frequency cortical activity |
| Filter timing | Offline zero-phase results never used to emulate a real-time controller | Future online branch needs causal filters and measured delay |
| Noise | Target ≤1 µV RMS over declared 0.5–40 Hz band with phantom inputs shorted, per channel | Board-level bench test pending; not inferred from ADC bit depth |
| Gain accuracy | Target ±5% at 10 Hz across all channels with a calibrated phantom | Bench test pending |
| Common-mode rejection | Target ≥80 dB at local line frequency under declared balanced-source impedance | Bench test pending; specify imbalance sensitivity separately |
| Crosstalk | Target ≤−60 dB at 10 Hz under declared loading | Bench test pending |
| Packet continuity | Log gaps, duplicate counters, resets and unsupported formats; never silently interpolate a gap | Software fixtures provided; physical dropout test pending |
| Marker timing | Target p95 absolute event error ≤20 ms for seconds-scale state experiments | Must measure physical stimulus onset and end-to-end error |
| Fast phase control | Not qualified by the 20 ms target | Sleep-phase or stimulation applications require a separate latency design |
| End-to-end delay | Target p95 ≤100 ms excluding the declared feature window | Hardware loopback and host-load tests pending |
| Windows | Initial quality windows 4 s; slower outcome features declared separately | Engineering default, not a clinically optimized time constant |
| Head fit | Intended adjustable circumference 520–640 mm | Assumed design envelope; anthropometric fit and pressure evaluation pending |
| Mass | Target head-worn mass ≤150 g; otherwise move OEM pod off-head | Weigh complete harness, leads, battery and wet contacts |
| Use duration | Initial supervised research sessions; target 2 h battery endurance with 20% reserve | No sleep/home-use qualification |
| Power | Supplier-compatible battery only; charging disconnected from the worn assembly | Confirm physical design prevents misuse; no USB tether to electrodes |
| Local storage | Raw bytes, configuration, events and analysis outputs stored locally with hashes | Offline parser/export supplied |
| Output | Research measurements and quality status | No diagnosis, emotion label or automatic treatment recommendation |

The ADS1299 is an eight-channel, simultaneous, 24-bit biopotential front end with selectable gain and sampling rates. Those component specifications do not establish the complete instrument's noise, isolation or effective resolution. [TI product and datasheet](https://www.ti.com/product/ADS1299)

## Harness and connections

This is the **logical net assignment**, not a substitute for checking the actual board's labelled connector and configuration readback. Never infer physical pin order from this table.

| Net | Electrode / connection | Logical channel mode |
|---|---|---|
| EEG1–EEG6 | Fp1, Fp2, F7, F8, O1, O2 respectively | Each active contact measured against M1 through verified common-reference routing |
| EOG7+ / EOG7− | Above / below one eye, distinct from EEG contacts | Differential vertical EOG, shared-reference switch disconnected |
| EOG8+ / EOG8− | Left / right outer canthus | Differential horizontal EOG, shared-reference switch disconnected |
| REF | M1 candidate reference contact | EEG reference only; record side and actual position |
| BIAS | Separate M2 candidate contact | OEM bias output only; not ground or a stimulation output |
| RADIO | OEM acquisition module to its dongle | Wireless serial link; not generic phone BLE |
| HOST | Dongle to host USB | No galvanic signal cable from host to worn electrodes |

That is 12 distinct contacts. Reference and bias placement can contribute artifacts and must be evaluated, not assumed ideal. Retain contact type, location, impedance check state and preparation metadata. Lead-off testing and bias circuits can apply currents: “recording only” does not mean electrically passive. Disable lead-off injection during analysis epochs and document any check epochs. Do not add custom current sources or stimulation outputs.

Use the supplier's touch-proof adapter system and documented lead connectors. Strain-relieve leads before their electrode carriers; separate battery strain from the signal bundle. R1 uses a hook-and-loop retained OEM case, so it introduces no electrical PCB. `mechanical/carrier.scad` and `carrier.svg` define the adjustable structural prototype. `mechanical/parameters.json` distinguishes assumed dimensions from measured dimensions.

## Firmware and host contract

Retain vendor firmware; do not flash the board as part of this release. Record the unit's startup identification, revision and register readback. Configure on the bench with the OEM GUI and independently verify each channel's gain, reference routing and test state. The mixed EEG/EOG configuration is not allowed to rely on factory defaults.

The supplied offline decoder supports the documented 33-byte Cyton frames, sign extension, per-channel scaling, framing recovery, counter discontinuities and raw auxiliary preservation. It decodes standard accelerometer auxiliary fields only for the corresponding footer. Timestamp/user-defined footer payloads remain raw and explicitly unsupported for their specialised interpretation. This is not a firmware port. [Data-format contract](https://docs.openbci.com/Cyton/CytonDataFormat/)

At 250 frames/s, 33 bytes/frame produces 8,250 bytes/s of raw transport data, or 29.7 MB/hour before filesystem and metadata overhead. UART 8-N-1 framing requires 82,500 bit/s, below the documented 115,200 baud link. This margin does not prove loss-free radio transport. The one-byte sample counter cannot identify loss of an exact multiple of 256 packets or distinguish every reset from wraparound; retain timing and session boundaries. Default-scale arithmetic gives approximately 0.02235 µV/count at reference 4.5 V and gain 24. Quantization size is not usable physiological resolution.

The host pipeline is: immutable raw bytes → parser/configuration → timing and quality masks → declared features → offline model → independent outcome evaluation. The present code stops at quality and record export. A later policy must reject missing/stale input, retain its version and evidence identity, log choices, allow participant stop, and expose the possibility that no measurement justifies an intervention. No medical actuation is implemented.

For multidevice research, use recorded clock offsets and a verified physical marker. LSL can carry synchronization information, but sensor acquisition and output-device delays still need measurement. [LSL timing documentation](https://labstreaminglayer.readthedocs.io/info/time_synchronization.html)

## Intervention interface

R1 includes **no electrical, magnetic or optical brain-stimulation hardware**. The research architecture can later record a reviewed phone-delivered behavioural or audio intervention through an event interface. The action record must include intended onset, measured onset when available, actual duration, content/version, participant acceptance and interruption. It must not equate a quiet signal with a successful treatment.

Candidate intervention research remains separate: fixed versus state-guided delivery of an established input, matched burden and attention, independent later outcomes, withdrawal and repeat-session evaluation. Sleep audio, tVNS, TMS and invasive stimulation are separate branches with different devices and protocols; this package does not provide their delivery settings.

## Verification and release boundary

The requirements register links each design objective to a concrete test and current evidence status. Software tests use synthetic fixtures and establish parser/calculation behaviour only. Physical acceptance requires the actual assembled unit, calibrated signal equipment, fit/cleaning assessment, electrical-safety review and protocol-specific research oversight. No human measurements were acquired in this release.

For a medical intended use, obtain jurisdiction-specific engineering and regulatory review. Candidate standards to evaluate include IEC 60601-1, IEC 60601-1-2, the EEG-specific IEC 60601-2-26, software lifecycle requirements, usability and biological evaluation. The full clauses have not been audited here and no compliance is claimed. FDA's January 2026 general-wellness policy is not permission to make mental-illness treatment claims. [FDA guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/general-wellness-policy-low-risk-devices), [ISO risk-management catalogue](https://www.iso.org/standard/72704.html), [ISO biological evaluation 2025](https://www.iso.org/standard/10993-1?browse=tc), [IEC software lifecycle catalogue](https://webstore.iec.ch/en/publication/6792).

The finished deliverable today is this reproducible design baseline and test software. The missing evidence is listed as work with acceptance criteria, rather than filled with invented passing results. A custom miniaturized board and production enclosure should be commissioned only after R1 establishes which channels and performance actually matter.
