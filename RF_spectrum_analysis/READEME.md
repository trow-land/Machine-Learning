# RF Modulation Classification

This project focuses on classifying radio frequency (RF) signals based on their modulation types using raw in-phase (I) and quadrature (Q) waveform data. The goal is to develop a robust signal classification pipeline using deep learning, starting with a basic 1D convolutional model.

---

## Overview

The dataset consists of over 2.5 million labelled I/Q signal samples stored in an HDF5 format. Each example contains 1024 complex-valued time steps and is associated with a modulation class and signal-to-noise ratio (SNR). 

A subset of five modulation types was selected for initial experimentation. Preliminary exploratory analysis has been carried out through waveform visualisation and constellation plotting.

---

## Progress So Far

- Extracted and filtered data from a large HDF5 archive
- Visualised waveform and constellation diagrams for multiple classes
- Preprocessed the data and built a PyTorch training pipeline
- Trained a baseline 1D CNN on a five-class classification task

Example output (time-domain and constellation plots):

![Modulation Examples](https://github.com/trow-land/Machine-Learning/blob/main/RF_spectrum_analysis/plots/spectrum_plots.png)

---

## Next Steps

- Improve and test alternative model architectures  
- Evaluate classification performance on a clean test set  
- Simulate and inject noise jamming into I/Q samples  
- Train a binary classifier to detect clean vs jammed signals  
- Analyse failure cases: which classes and SNR levels are most affected?

---

