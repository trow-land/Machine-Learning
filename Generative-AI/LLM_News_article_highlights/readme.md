# News Article Highlights Summarisation Project

## Overview

This project focuses on fine-tuning a pre-trained BART large language model to generate concise, one- or two-sentence highlights from CNN and DailyMail news articles. The goal is to improve the model’s ability to summarise lengthy articles while maintaining key information. The project evaluates the performance of the fine-tuned model using the ROUGE metric and compares its generated summaries to human-written highlights.

## Project Structure

- **News_article_highlights.ipynb**: Jupyter notebook containing the implementation for generating summaries of news articles using a pre-trained language model. It includes data loading, preprocessing, tokenisation, fine-tuning, summary generation, and result evaluation.
- **dataset**: The dataset used for this project is the [CNN_DailyMail](https://huggingface.co/datasets/abisee/cnn_dailymail) dataset from Hugging Face.

## Dataset

The dataset consists of a collection of news articles and their respective human-written highlights. The highlights are short summaries written by the article authors and serve as ground truth references. The dataset was created to train large language models to summarise long text inputs into brief, informative highlights.

- **Articles**: Full-length news articles used as input.
- **Highlights**: Human-written summaries used for evaluation and comparison with the model's output.

### Dataset Statistics:
- **Training Samples**: 287,113
- **Validation Samples**: 13,368
- **Test Samples**: 11,490

## Requirements

To run the project, you'll need the following Python libraries installed:

- `transformers`: For loading and fine-tuning the pre-trained language model.
- `datasets`: For loading and managing the dataset.
- `torch`: For tensor operations and model training.
- `evaluate`: For calculating metrics such as ROUGE.
- `tqdm`: For progress bars.
- `pandas`: For data manipulation.

## Model Used

The project utilises a pre-trained BART model from the Hugging Face library for text summarisation. Specifically:

- **Model**: `facebook/bart-large-cnn`
- **Tokenizer**: `facebook/bart-large-cnn`

The model was chosen for its effectiveness in summarisation tasks and its ability to handle relatively long text inputs.

## Preprocessing

1. **Tokenization**: Each article is tokenized using the model's tokenizer, with a maximum token length of 1024 to fit within the model's input size limits.
2. **Truncation**: Articles that exceed the token length are truncated to ensure efficient processing.
3. **Batch Padding**: Uses a data collator to pad and batch tokenized inputs efficiently.

> **Note:** Initially, the maximum token length was set to 512, but it was increased to 1024 to accommodate longer input articles and improve summary quality.

## Fine-Tuning

The model was fine-tuned using the `Trainer` API from the `transformers` library. Training parameters included:
- Mixed-precision training (FP16) for efficiency.
- Regular evaluation during training.
- Batch size and learning rate chosen for balanced performance and speed.

## Evaluation

After generating summaries for the test set, the following metrics were used for evaluation:

- **ROUGE-1** (Unigram overlap)
- **ROUGE-2** (Bigram overlap)
- **ROUGE-L** (Longest Common Subsequence)

### Results

| **Metric**    | **Score** |
|--------------|-----------|
| ROUGE-1      | 0.3557    |
| ROUGE-2      | 0.1579    |
| ROUGE-L      | 0.2630    |
| ROUGE-Lsum   | 0.2622    |

The generated summaries often captured key points effectively, but there was some variation from the human-written highlights, resulting in moderate ROUGE scores.

## Example Outputs

The table below shows examples of generated summaries compared to the original highlights from the dataset:

## Example Outputs

The table below shows examples of generated summaries compared to the original highlights from the dataset:  

<details>
  <summary><strong>Example 1: Anthony Ray Hinton Case</strong></summary>

**Input Prompt:**  
> *(CNN)* Anthony Ray Hinton is thankful to be free after nearly 30 years on Alabama's death row for murders he says he didn't commit. And incredulous that it took so long. Hinton, 58, looked up, took in the sunshine and thanked God and his lawyers Friday morning outside the county jail in Birmingham, minutes after taking his first steps as a free man since 1985. He spoke of unjustly losing three decades of his life, under fear of execution, for something he didn't do. "All they had to do was to test the gun, but when you think you're high and mighty and you're above the law, you don't have to answer to nobody," Hinton told reporters. "But I've got news for you -- everybody that played a part in sending me to death row, you will answer to God." Jefferson County Circuit Court Judge Laura Petro had ordered Hinton released after granting the state's motion to dismiss charges against him. Hinton was convicted of murder in the 1985 deaths of two Birmingham-area, fast-food restaurant managers, John Davidson and Thomas Wayne Vason. But a new trial was ordered in 2014 after firearms experts testified 12 years earlier that the revolver Hinton was said to have used in the crimes could not be matched to evidence in either case, and the two killings couldn't be linked to each other. "Death Row Stories": Hard questions about the U.S. capital punishment system . The state then declined to re-prosecute the case. Hinton was 29 at the time of the killings and had always maintained his innocence, said the Equal Justice Initiative, a group that helped win his release. "Race, poverty, inadequate legal assistance, and prosecutorial indifference to innocence conspired to create a textbook example of injustice," Bryan Stevenson, the group's executive director and Hinton's lead attorney, said of his African-American client. "I can't think of a case that more urgently dramatizes the need for reform than what has happened to Anthony Ray Hinton." Stevenson said the "refusal of state prosecutors to re-examine this case despite persuasive and reliable evidence of innocence is disappointing and troubling." Amnesty report: Executions down but death sentences on the rise . Dressed in a dark suit and blue shirt, Hinton praised God for his release, saying he was sent "not just a lawyer, but the best lawyers." He said he will continue to pray for the families of the murder victims. Both he and those families have suffered a miscarriage of justice, he said. "For all of us that say that we believe in justice, this is the case to start showing, because I shouldn't have (sat) on death row for 30 years," he said. Woman who spent 22 years on death row has case tossed . Hinton was accompanied Friday by two of his sisters, one of whom still lives in the Birmingham area. Other siblings will fly to the area to see him soon, Stevenson said. His mother, with whom he lived at the time of his arrest, is no longer living, according to the lawyer. Hinton planned to spend at least this weekend at the home of a close friend. He will meet with his attorneys Monday to start planning for his immediate needs, such as obtaining identification and getting a health checkup, Stevenson said. The plan now is to spend a few weeks to get oriented with freedom and "sort out what he wants to do," Stevenson said.

---

**Baseline Human Summary:**  
> *Anthony Ray Hinton goes free Friday, decades after conviction for two murders. Court ordered new trial in 2014, years after gun experts testified on his behalf. Prosecution moved to dismiss charges this year.*  

---

**Fine-Tuned BART Model Summary:**  
> *Anthony Ray Hinton was convicted of murder in the 1985 deaths of two Birmingham-area fast-food restaurant managers. A new trial was ordered in 2014 after firearms experts testified 12 years earlier that the revolver could not be matched to evidence in either case. The state then declined to re-prosecute the case.*  

</details>

<details>
  <summary><strong>Example 2: Aaron Hernandez Case</strong></summary>

**Input Prompt:**  
> *(CNN)* Former New England Patriots star Aaron Hernandez will need to keep his lawyers even after being convicted of murder and other charges in the death of Odin Lloyd. The 25-year-old potentially faces three more trials -- one criminal and two civil actions. Next up is another murder trial in which he is accused of killing two men and wounding another person near a Boston nightclub in July 2012. Prosecutors have said Hernandez fatally shot Daniel de Abreu and Safiro Furtado when he fired into their 2003 BMW.  Another passenger was wounded and two others were uninjured. Hernandez pleaded not guilty at his arraignment. The trial was originally slated for May 28, but Jake Wark, spokesman for the Suffolk County District Attorney's Office, said Wednesday the trial had been postponed and no new date had been set. "We expect to select a new court date in the coming days and then set the amended trial track. The Suffolk indictments allege two counts of first-degree murder for the July 16, 2012, shooting deaths of Daniel de Abreu and Safiro Furtado in Boston's South End; three counts of armed assault with intent to murder and one count of assault and battery by means of a dangerous weapon for shots fired at three surviving victims; and one count of unlawful possession of a firearm," he said. The families of de Abreu and Furtado filed civil suits against Hernandez, and a judge froze his $5 million in assets, pending the outcome of the double-murder trial. The freeze includes the disputed $3.3 million signing bonus payment Hernandez claims he is owed by the New England Patriots. Hernandez is also being sued by a man who claims Hernandez shot him while they were in a limousine in Miami in February 2013. Alexander Bradley claims the then-New England Patriot tight end wounded him after the two got into a fight at a Miami strip club. In a lawsuit filed four months later, Bradley said Hernandez fired at him during a limo ride after leaving the club and that Hernandez intentionally "possessed a gun which he was not legally licensed to have." Hernandez's lawyers have argued he couldn't defend himself properly while on trial in Massachusetts. There was no criminal charge in the case. And then there is the grievance over unpaid bonus money filed by the NFL players union on behalf of Hernandez, who signed a contract in 2012 that potentially was worth more than $40 million. If the grievance is heard by the league, Hernandez will be represented by the the National Football League Players' Association. Who was Odin Lloyd? CNN's Lawrence Crook contributed to this report.

---

**Baseline Human Summary:**  
> *Aaron Hernandez has been found guilty in Odin Lloyd's death, but his troubles are not over . He also faces murder charges in Suffolk County, Massachusetts, but trial was postponed . In addition, Hernandez will face two civil lawsuits; one is in relation to Suffolk County case .*  

---

**Fine-Tuned BART Model Summary:**  
> *Aaron Hernandez potentially faces three more trials -- one criminal and two civil actions. He is accused of killing two men and wounding another person near a Boston nightclub in July 2012. Prosecutors have said Hernandez fatally shot Daniel de Abreu and Safiro Furtado when he fired into their 2003 BMW.*  

</details>


## Challenges

- **Poor Human Summaries:** Some of the observed human baseline summaries miss some context from the original article which unfairly penalises the finetuned models.
- **Input Truncation:** Long articles are truncated to fit the model’s input limit, potentially omitting relevant information.
- **Highlight Lengths:** Some human-written highlights are longer than expected (3–4 sentences), which may confuse the model when training it to generate shorter outputs.
- **Evaluation Limitations:** Condensing long texts into brief highlights is inherently challenging, and differences in wording negatively impact ROUGE scores despite semantic similarity.

## Future Work

- Experiment with hyperparameter tuning to improve summarisation quality.
- Train on a larger portion or the entirety of the CNN/DailyMail dataset to enhance generalisation.
- Explore advanced techniques like prompt engineering or model ensembling for better performance.

## Conclusion

This project demonstrates how to fine-tune a pre-trained BART model for summarising long news articles into short highlights. While the model achieves reasonable ROUGE scores, improvements are possible through further fine-tuning and better handling of lengthy input texts.

## References

- Hugging Face Transformers: [https://huggingface.co/transformers/](https://huggingface.co/transformers/)
- CNN/DailyMail Dataset: [https://huggingface.co/datasets/cnn_dailymail](https://huggingface.co/datasets/cnn_dailymail)
