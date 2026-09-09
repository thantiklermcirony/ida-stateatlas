# IDA transport and quality reference software

Python 3.12+; standard library only. The software reads saved binary files. It does not connect to, configure or actuate hardware. Use the OEM acquisition software for actual board recording and configuration, and export the documented raw binary format before using this decoder. A text/CSV export must not be renamed `.bin`.

From the project root:

```sh
python -m unittest discover -s engineering/software -p "test_*.py" -v
python engineering/software/run_bench.py
python engineering/software/ida_capture.py --binary engineering/bench/synthetic_clean.bin --config engineering/bench/synthetic_config.json --out local-results/synthetic_capture.json
```

The included configuration belongs to the synthetic fixture. It is not verified configuration for an actual device. Replace it with audited gain, reference and channel labels when analysing a physical recording. Vendor GUI configuration and register readback remain necessary.

The 13 tests cover numeric extremes, scaling, all chunk split positions, framing recovery, counter wrap/gaps/duplicates, trailing bytes, auxiliary-format boundaries and quality rejection. Five deterministic fault scenarios make the expected quality behaviour inspectable.

Quality thresholds are simple engineering candidates. They do not prove a channel is neural or free from eye/muscle contamination. The parser preserves raw auxiliary bytes; it does not implement every specialised timestamp format. There is no transport CRC in this packet specification, so some corruptions remain undetectable. Modulo counters cannot reveal every reset or loss. No acquisition timestamps are fabricated from frame indices.

Future live integration should use a pinned supported driver such as BrainFlow, validated against the same fixtures and the actual unit. It needs an explicit raw recording/export path, real timing evidence and signal-quality integration before a real-time IDA policy is considered. No untested driver is presented as operational here.
