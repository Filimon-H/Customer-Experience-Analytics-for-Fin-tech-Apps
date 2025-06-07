# src/theme_extraction.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

def extract_keywords_tfidf(df, text_column='review', max_features=1000, top_n=10):
    """
    Extract top TF-IDF keywords per bank.
    
    Parameters:
    - df: DataFrame with at least 'bank' and 'review' columns
    - text_column: name of the column containing the review text
    - max_features: max number of features for TF-IDF
    - top_n: number of top keywords to extract per bank

    Returns:
    - dict of bank -> top N keywords
    """
    results = defaultdict(list)

    for bank, group in df.groupby("bank"):
        reviews = group[text_column].fillna("").tolist()
        
        vectorizer = TfidfVectorizer(stop_words="english", max_features=max_features, ngram_range=(1, 2))
        tfidf_matrix = vectorizer.fit_transform(reviews)
        scores = tfidf_matrix.sum(axis=0).A1
        vocab = vectorizer.get_feature_names_out()
        
        keyword_scores = list(zip(vocab, scores))
        keyword_scores.sort(key=lambda x: x[1], reverse=True)
        
        results[bank] = [kw for kw, _ in keyword_scores[:top_n]]
    
    return dict(results)
