# HuffPost News Headline Classifier

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Data](#data)
6. [Model Architecture](#model-architecture)
7. [Training and Evaluation](#training-and-evaluation)
8. [Results](#results)
9. [Future Work](#future-work)
10. [License](#license)


## Introduction

This project is to serve as a refresher for basic NLP concepts such as exploratory data analysis, label encoding as tokenization as well as exploring how some simple model architectures compare when tasked with classifying a news headline from the [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) found on Kaggle.

### Objectives

- Explore the data and understand the dataset and its imbalanced
- Prepare the dataset for training using TensorFlow 
- Train various models and evaluate their performance

## Requirements

- Python 3.10
- TensorFlow 2.10.10
- See [requirements.txt](NLP\requirements.txt)

## Installation


```bash
pip install -r requirements.txt
```

The project is conducted through jupyter notebook, so after the correct python version and modules are downloaded cycle through the notebook cells.

## Usage

The project is conducted through jupyter notebook, so after the correct python version and modules are downloaded cycle through the notebook cells.


## Data

### Overview

The [News Categories Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) features approximately 210k news headlines from HuffPost, spanning from 2012 to 2022. It serves as a comprehensive benchmark for various computational linguistic tasks.

### Attributes

Each record in the dataset contains the following fields:
- **Category**: The section under which the article is published.
- **Headline**: The title of the article.
- **Authors**: List of contributing authors.
- **Link**: URL to the original article.
- **Short Description**: A summary of the article.
- **Date**: The article's publication date.

### Categories

The dataset encompasses 42 unique news categories. The top three categories by article count are:
- **POLITICS**: 35,602 articles
- **WELLNESS**: 17,945 articles
- **ENTERTAINMENT**: 17,362 articles



## Model Architecture

As this was a practice project several simple architectures were compared such as:

- RNN
- LSTM
- Convolutional
- Hybrid

## Training and Evaluation

Training was initially conducted over 10 epochs on an Nvidia GeForce GTX 1070

### Metrics

- Training Accuracy
- Training Loss
- Validation Acccury
- Validation Loss

## Results

All of the models acheived similar validation accuracy scores of around 57% but they all suffered from overfitting. All models suffered from overfitting some more than others. Further architecture optimisation could reduce this.

For all models the learning plateaued after the 3rd epoch, from then on overfitting became more apparent as the training accuracy increased. 

## Future Work

- Compare with a Transformer based architecture and with a pre-trained weights
- Examine the impact of further feature engineering

## License

This project is licensed under the [MIT License](LICENSE).


