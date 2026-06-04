# Week 5 – Fine-Tuning Large Language Models

## Objective

The objective of this assignment was to evaluate and fine-tune a pretrained Large Language Model (LLM) for marketing email generation using a Parameter Efficient Fine-Tuning (PEFT) approach.

---

## Dataset

Source: Hugging Face

Dataset: `kuokxuen/marketing_dataset`

Features:

* Product Name
* Product Description

Target:

* Marketing Email

Records: 100

---

## Model

Base Model:

`Qwen/Qwen2.5-1.5B-Instruct`

Reason for Selection:

* Strong text generation capabilities
* Compatible with Kaggle GPU resources
* Suitable for LoRA fine-tuning

---

## Fine-Tuning Method

Parameter Efficient Fine-Tuning (PEFT)

Technique:

LoRA (Low Rank Adaptation)

Advantages:

* Reduced GPU requirements
* Faster training
* Smaller storage footprint
* Efficient adaptation of foundation models

---

## Workflow

1. Dataset Exploration
2. Base Model Evaluation
3. Prompt Construction
4. Tokenization
5. LoRA Configuration
6. Fine-Tuning
7. Post-Training Evaluation
8. Prompt Engineering Analysis
9. Hyperparameter Analysis
10. Bias and Risk Evaluation

---

## Results

Training Configuration:

* Epochs: 1
* Learning Rate: 2e-4
* Batch Size: 2

Training Outcome:

* Fine-tuning completed successfully
* Marketing email generation quality improved
* Outputs became more aligned with dataset style

---

## Key Learnings

* Foundation Model Adaptation
* Supervised Fine-Tuning (SFT)
* Tokenization
* LoRA and PEFT
* Prompt Engineering
* Hyperparameter Tuning
* Responsible AI Evaluation

---

## Files

* `Marketing_Email_Finetuning.ipynb` – Complete implementation and analysis notebook
