# sentiment_analysis.py

import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Make sure VADER lexicon is downloaded
nltk.download("vader_lexicon", quiet=True)

# Initialize NLTK VADER analyzer
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    """
    Analyze sentiment using NLTK VADER and return compound score + label.
    """
    if not isinstance(text, str):
        return {'score': 0.0, 'label': 'neutral'}

    scores = analyzer.polarity_scores(text)
    compound = scores['compound']

    if compound >= 0.05:
        label = 'positive'
    elif compound <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'

    return {'score': compound, 'label': label}

def add_sentiment_columns(df):
    """
    Apply sentiment analysis to the detected review text column.
    """
    # Try common column names
    possible_cols = ['review_text', 'review', 'text', 'comment']
    review_col = None

    for col in df.columns:
        if col.lower() in possible_cols:
            review_col = col
            break

    if review_col is None:
        raise KeyError(f"❌ No valid review column found in: {df.columns.tolist()}")

    sentiments = df[review_col].apply(analyze_sentiment)
    df['sentiment_score'] = sentiments.apply(lambda x: x['score'])
    df['sentiment_label'] = sentiments.apply(lambda x: x['label'])
    return df


def process_and_save(input_path, output_path):
    """
    Load input CSV, apply sentiment analysis, and save output.
    """
    df = pd.read_csv(input_path)
    df = add_sentiment_columns(df)
    df.to_csv(output_path, index=False)
    print(f"✅ Sentiment-enriched file saved to: {output_path}")
