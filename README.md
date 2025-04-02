---
title: Explain My Data
emoji: 📊
colorFrom: blue
colorTo: teal
sdk: gradio
sdk_version: "4.15.0"
app_file: app.py
pinned: false
---

# 📊 Explain My Data – AI-Powered CSV Profiler

**Explain My Data** is a powerful and intuitive tool that helps you analyze, understand, and visualize tabular data (CSV) using the power of AI and data profiling.

## 🚀 Features

- ✅ Upload any CSV file
- ✅ Automatically generate data summaries (column types, stats, nulls)
- ✅ Instant visualizations (histograms for numeric columns)
- ✅ AI-generated plain English insights using `MBZUAI/LaMini-Flan-T5-248M`
- ✅ Interactive column selection for custom plots
- ✅ Streamlined UI using Gradio

## 🧠 Powered by

- [LangChain](https://github.com/hwchase17/langchain) (logic orchestration)
- [Transformers](https://huggingface.co/docs/transformers) for LLM inference
- [MBZUAI/LaMini-Flan-T5-248M](https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M) — open, fast, and instruction-tuned LLM
- [Pandas](https://pandas.pydata.org/) for data analysis
- [Matplotlib](https://matplotlib.org/) for visualizations
- [Gradio](https://gradio.app/) for the web interface

## 📸 Demo

| Summary View | Plot & Insights |
|--------------|-----------------|
| ![Summary](./screenshots/summary.png) | ![Insights](./screenshots/insights.png) |

> _Note: You can take screenshots of your running app and save them in `/screenshots/` to display here._

## 📁 How to Use

1. Upload a CSV file (e.g. `synthetic_customer_data.csv`)
2. View automatic summary of dataset
3. See a distribution plot of the first numeric column
4. Select other columns from the dropdown to explore visually
5. Click **"Generate AI Insights"** to get meaningful takeaways from your data

## 🧰 Installation

```bash
git clone https://github.com/TrishKedi/explain-my-data.git
cd explain-my-data
pip install -r requirements.txt
python app.py
