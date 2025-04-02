from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

class FlanLLM:
    def __init__(self, model_id="MBZUAI/LaMini-Flan-T5-248M", device=-1):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
        self.pipeline = pipeline(
            "text2text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            device=device  # -1 for CPU
        )

    def __call__(self, summary: str) -> str:
        prompt = f"""
You are a data analyst. Analyze the dataset summary below and provide 3 key insights.

### Dataset Summary:
{summary}

### Instructions:
- Do not repeat the raw stats
- Explain patterns, correlations, outliers, imbalances
- Write in clear, plain English
- Use bullet points
"""
        result = self.pipeline(prompt.strip(), max_new_tokens=256, temperature=0.3)
        return result[0]["generated_text"]
