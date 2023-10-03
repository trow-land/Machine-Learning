# House Price Prediction


## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data](#data)
6. [Model Architecture](#model-architecture)
7. [Training and Evaluation](#training-and-evaluation)
8. [Results](#results)


## Introduction

Briefly introduce the project here. What is it about? What problem does it solve?

### Objectives

- Refresh my skills by comparing multiple regression algorithms on the Housing.csv dataset
- Train models on local GPU 
- Inspect, clean and process dataset with pandas and scikit-learn

## Requirements

- Python 3.10
- TensorFlow 2.10.0
- see requirements.txt

## Installation

Installation can be conducted with the following command:

```bash
pip install -r requirements.txt
```

## Usage

This project will be conducted in the jupyter notebook [housePricesRegression.ipynb](code/housePricesRegression.ipynb) for ease of visualisation and comparison.



## Data

The dataset used was downloaded from [kaggle](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset). The dataset consists of multiple features targeting a predicted house price.

### Features

- Area
- Bedrooms
- Bathrooms
- Mainroad
- Stories
- Guestroom 
- Basement 
- Hotwaterheating 
- Airconditioning 
- Parking 
- Prefarea 
- Furnishingstatus



## Models Tested

Four models were compared for this task

- Linear Regression
- Random Forrest Regression
- Elastic Net Regression 
- Neural Network Regression


## Training and Evaluation

Model.fit() was used to train all models on the same dataset. 

Only an extremely basic neural network was made for this project and trained for 250 epochs. 

Evaluation was carried out both quantatively and qualitavely with a comparison between models and plots comparing predicted price values and true price values.

### Metrics

- Mean Squared Error
- Mean Absolute Error
- R2 Error

## Results

Linear Regression = MSE(1754318687330.668), MAE(970043.4039201643), R2(0.6529242642153176)
Random Forrest Regression = MSE(1942301284715.1775), MAE(1019856.0883792049), R2(0.6157336449891048)
Elastic Net = MSE(1993228920637.3289), MAE(1004041.6089634736), R2(0.6056580829848317)
Neural Network = MSE(1766810339382.3682), MAE(971789.9678899082), R2(0.6504529063267421)

