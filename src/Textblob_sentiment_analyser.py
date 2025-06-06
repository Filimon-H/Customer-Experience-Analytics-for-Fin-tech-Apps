# sentiment_analysis.py

import pandas as pd
from textblob import TextBlob
import nltk
nltk.download('punkt')

def analyze_sentiment(text):
    """
    Compute sentiment polarity score and label using TextBlob.
    """
    if not isinstance(text, str) or text.strip() == "":
        return {'score': 0.0, 'label': 'neutral'}

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        label = 'positive'
    elif polarity < -0.1:
        label = 'negative'
    else:
        label = 'neutral'

    return {'score': polarity, 'label': label}

def add_sentiment_columns(df):
    """
    Apply sentiment analysis to a DataFrame of reviews.
    """
    sentiments = df['review'].apply(analyze_sentiment)
    df['sentiment_score'] = sentiments.apply(lambda x: x['score'])
    df['sentiment_label'] = sentiments.apply(lambda x: x['label'])
    return df

def process_and_save(input_path, output_path):
    """
    Load cleaned reviews, add sentiment columns, and save new file.
    """
    df = pd.read_csv(input_path)
    df = add_sentiment_columns(df)
    df.to_csv(output_path, index=False)
    print(f"✅ Sentiment-enriched file saved to: {output_path}")
