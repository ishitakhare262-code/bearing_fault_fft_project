# Induction Motor Bearing Fault Diagnosis (CWRU Dataset)

This repository contains Python scripts for analyzing drive-end bearing faults using time-domain signal processing and Fast Fourier Transform (FFT) analysis on the CWRU dataset.

## Project Structure
* `inspect_data.py`: Loads MATLAB `.mat` files, extracts raw signal arrays, and inspects dataset structure.
* `step2_plot_time.py`: Plots and compares healthy vs. faulty time-domain waveforms to analyze vibration/current amplitude changes.
* `step 3`: Applies Fast Fourier Transform (FFT) to convert time-domain signals into the frequency domain and isolate fault characteristic frequencies.

## Requirements & Libraries
* Python 3.x
* `numpy`
* `scipy`
* `matplotlib`

## Requirements

- Python 3.8+
- numpy, scipy, matplotlib (installed automatically)

## Installation

```bash
pip install git+https://github.com/ishitakhare262-code/bearing_fault_fft_project.git
```

## Data

Download the CWRU bearing dataset and place `97.mat`, `105.mat`, `118.mat` and `130.mat` in a folder (for example `data/`). The data files are not included in the package.

## How to Run

```bash
cwru-inspect --data-dir path/to/data
cwru-plot-time --data-dir path/to/data
```

If `--data-dir` is omitted, the commands look for a `data` folder in the current directory.
