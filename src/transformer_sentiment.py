# src/transformer_sentiment.py

import pandas as pd
import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification

# Load tokenizer and model (do this once)
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """
    Perform sentiment analysis using DistilBERT SST-2.
    Returns score and label (positive/negative).
    """
    if not isinstance(text, str) or len(text.strip()) == 0:
        return {'score': 0.0, 'label': 'neutral'}

    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        logits = model(**inputs).logits

    predicted_class_id = logits.argmax().item()
    label = model.config.id2label[predicted_class_id]
    score = torch.nn.functional.softmax(logits, dim=1).squeeze()[predicted_class_id].item()

    return {'score': score, 'label': label.lower()}

def add_sentiment_columns(df):
    """
    Add DistilBERT sentiment scores and labels to DataFrame.
    """
    sentiments = df["review"].apply(analyze_sentiment)
    df["sentiment_score"] = sentiments.apply(lambda x: x["score"])
    df["sentiment_label"] = sentiments.apply(lambda x: x["label"])
    return df

def process_and_save(input_path, output_path):
    """
    Load CSV, run DistilBERT sentiment, save new CSV.
    """
    df = pd.read_csv(input_path)
    df = add_sentiment_columns(df)
    df.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path}")
