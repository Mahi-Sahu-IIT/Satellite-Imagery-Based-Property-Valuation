# Satellite-Imagery-Based-Property-Valuation
# Overview

This project implements a multimodal deep learning regression model using PyTorch, combining image data and tabular numerical features to predict a continuous target variable. The model is trained end-to-end and evaluated using RMSE and R² score.

# Dataset

Images: RGB images (processed using CNN)

Tabular data: Numerical features from CSV

Target: Continuous value (regression task)

Dataset size: ~16,000 samples

# Model Architecture

Image branch: CNN feature extractor

Tabular branch: Fully connected layers

Fusion: Concatenation of image and tabular embeddings

Output: Single regression neuron

# Training Details

Framework: PyTorch

Loss Function: Mean Squared Error (MSE)

Optimizer: Adam

Batch Size: User-defined

Device: CPU / GPU (if available)

# Evaluation Metrics

RMSE (Root Mean Squared Error)

R² Score (Coefficient of Determination)

These metrics are computed after training on the test dataset.
# How to Run

1. Clone the repository

2.Ensures correct project structure and paths.

Create environment (recommended)

Avoids dependency conflicts.

3.Install dependencies

Installs required libraries.

4.Prepare data
Run data_fetcher.py file in python to fetch images. I had used mapbox token to do so. you may use your own API token.
Images must align with CSV entries.

5.Run the notebook

jupyter notebook
Open the notebook and run cells top to bottom.

6.Train & evaluate
Wait for training to finish ([*] means running).
RMSE and R² are printed after training completes.

# Notes

Training time depends on hardware (CPU/GPU).

Ensure correct image paths and CSV file mappings.

Model supports easy extension to GPU training.
# Author

Mahi Sahu
IIT Roorkee
