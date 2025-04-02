import gradio as gr
import pandas as pd
from data_profiler import summarize_dataframe, generate_histogram
from llm_analyzer import FlanLLM

llm = FlanLLM()
df_store = {}

def on_csv_upload(file):
    if file is None:
        return gr.update(), "", None, "", gr.update()

    df = pd.read_csv(file.name)
    df_store["df"] = df

    summary = summarize_dataframe(df)
    columns = df.columns.tolist()

    # Get first numeric column (if exists)
    numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    default_col = numeric_columns[0] if numeric_columns else None

    # Generate default plot or fallback message
    plot = generate_histogram(df, default_col) if default_col else None
    plot_label = f"Distribution of '{default_col}'" if default_col else "No numeric column to plot"

    return (
        gr.update(choices=columns, value=default_col),
        summary,
        plot,
        plot_label,
        gr.update(interactive=True)  # Enable insights button
    )

def on_column_select(column):
    df = df_store.get("df")
    if df is not None and column in df.columns:
        return generate_histogram(df, column), f"Distribution of '{column}'"
    return None, "No plot available"

def on_generate_insights(summary):
    prompt = f"""
You are a data analyst helping a business understand their data.

Below is a summary of each column in a dataset. Your job is to extract **3 key insights** from it in plain English.

Be analytical. Focus on:
- Skewed distributions
- Missing data
- Outliers or unusual patterns
- Imbalances
- Anything that might affect decision-making or modeling

Do NOT repeat raw stats. Be insightful.

### Dataset Summary:
{summary}

Now generate 3 key insights:
"""
    return llm(prompt)

with gr.Blocks() as demo:
    gr.Markdown("# 📊 Explain My Data – AI-Powered CSV Profiler")

    file_input = gr.File(label="Upload CSV")

    with gr.Row():
        summary_text = gr.Textbox(label="📄 Summary", lines=20, interactive=False)
        with gr.Column():
            plot_output = gr.Image(label="📊 Distribution Plot", height=400)
            plot_label = gr.Textbox(visible=False)  # for alt-text if needed

    column_dropdown = gr.Dropdown(label="Select Column to Plot", choices=[], interactive=True)
    generate_button = gr.Button("🔍 Generate AI Insights", interactive=False)
    insights_text = gr.Textbox(label="🤖 AI Insights", lines=6, interactive=False)

    # File Upload Triggers Summary + Default Plot + Dropdown
    file_input.change(
        fn=on_csv_upload,
        inputs=file_input,
        outputs=[column_dropdown, summary_text, plot_output, plot_label, generate_button]
    )

    # Column selection triggers re-plot
    column_dropdown.change(
        fn=on_column_select,
        inputs=column_dropdown,
        outputs=[plot_output, plot_label]
    )

    # Insight button triggers LLM analysis
    generate_button.click(
        fn=on_generate_insights,
        inputs=summary_text,
        outputs=insights_text
    )

demo.launch()
