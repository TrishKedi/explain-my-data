import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
from PIL import Image


def summarize_dataframe(df: pd.DataFrame) -> str:
    summary = []
    for col in df.columns:
        desc = df[col].describe(include='all')
        nulls = df[col].isnull().mean() * 100
        dtype = df[col].dtype
        summary.append(f"Column: {col}\nType: {dtype}\n{desc.to_string()}\nMissing: {nulls:.2f}%\n")
    return "\n\n".join(summary)

def generate_histogram(df: pd.DataFrame, column: str):
    plt.figure(figsize=(6, 4))
    df[column].hist(bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

    # Save to BytesIO and convert to PIL
    buf = BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return Image.open(buf)  # ✅ Return PIL Image




