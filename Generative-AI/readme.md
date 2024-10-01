# News Article Highlights Summarisation Project

## Overview

This project focuses tune a model to make concise, one- or two-sentence highlights using a pre-trained large language model from CNN and dailymail news articles. The project evaluates the performance of a base summarisation model on a dataset of news articles and compares its summaries to human-written highlights.

## Project Structure

- **News_article_highlights.ipynb**: Jupyter notebook containing the implementation for generating summaries of news articles using a pre-trained language model. It includes preprocessing, tokenization, summary generation, and result evaluation.
- **dataset**: The dataset used for this project was the [CNN_DailyMail](https://huggingface.co/datasets/abisee/cnn_dailymail) dataset from huggingface

## Dataset

The dataset consists of a collection of news articles and their respective human-written highlights. The documentation describes the highlights as short summaries as written by the article author and that the dataset was created in an attempt to teach LLMs to summarise large inputs of text into 1 or 2 sentences.

- **Articles**: Full-length news articles used as input.
- **Highlights**: The human-written summaries used for evaluation and comparison with the model's output.

## Requirements

To run the project, you'll need the following Python libraries installed:

- `transformers`: For loading the pre-trained language model.
- `datasets`: For loading and managing the dataset.
- `torch`: For PyTorch backend operations.

## Model Used

The project utilises a pre-trained language model from the Hugging Face library for text summarisation. Specifically:

- **Model**: `BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")`
- **Tokenizer**: `AutoTokenizer.from_pretrained("facebook/bart-large-cnn")`

## Preprocessing

1. **Tokenization**: Each article is tokenized using the model's tokenizer, with a maximum token length of 1024 to fit within the model's input size limits.
2. **Truncation**: Articles that exceed the token length are truncated to ensure efficient processing.

Initially the input dataset was tokenized to max length of 512 but that was increased to max permissable value of 1024 for BART to allow for the long input article lengths.



## Evaluation

After generating summaries for 100 example articles, the following metrics are used for evaluation:

- **Comparison to Reference Highlights**: The generated summaries are compared to the human-written highlights using manual inspection and by the ROUGE metric.

## Results

The table below provides an example of the generated summaries vs. the original highlights from the dataset:

| **Article** | **Human-written Highlights** | **Model-generated Summary** |
|-------------|------------------------------|-----------------------------|
| Article 1   | Highlight 1                   | Summary 1                   |
| Article 2   | Highlight 2                   | Summary 2                   |

## Challenges

- **Input Truncation**: Some articles are too long and are truncated to fit the model's input length limit. This may lead to incomplete summaries.
- **Highlight lengths**: Upon inspection a lot of the human written article highlights are 3 or 4 sentences in length which when used in training may confuse the model as to the specific task required.
- **Evaluation**: Condending such a long article into a few sentences is hard. Often the model will have picked out the important points but the language used might be different from that in the human written label and as such the ROUGE score is negatively affected.

## Future Work

- Seek further opportunities for improvement by hyperparameter tuning
- Train on a larger subset (or all) of the cnn_dailymail dataset

## Conclusion

This project provides a working example of using pre-trained models for summarizing long news articles into short highlights. While the model generates readable summaries, there are areas for improvement, such as handling long inputs more effectively and improving output quality through fine-tuning.

## References

- Hugging Face Transformers: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
- CNN/Daily Mail Dataset: [https://huggingface.co/datasets/cnn_dailymail](https://huggingface.co/datasets/cnn_dailymail)
