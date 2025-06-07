import spacy
import pandas as pd

# Load English spaCy model
nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])  # We only need tokenization & lemmatization

def clean_text_spacy(text):
    """
    Tokenizes, removes stop words, and lemmatizes text using spaCy.
    Keeps only alphabetic tokens and excludes stopwords and punctuation.
    """
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.is_alpha and not token.is_stop
    ]
    return " ".join(tokens)

#def preprocess_reviews(df, text_column="review"):
    """
    Applies spaCy-based preprocessing to a specified text column in a DataFrame.
    Adds a new column called 'cleaned_review'.
    """
    df["cleaned_review"] = df[text_column].astype(str).apply(clean_text_spacy)
    return df

def preprocess_reviews(df, text_column):
    import spacy
    nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
    
    def clean_text(text):
        doc = nlp(str(text))
        tokens = [
            token.lemma_.lower()
            for token in doc
            if not token.is_stop and not token.is_punct and token.is_alpha
        ]
        return " ".join(tokens)
    
    df["cleaned_review"] = df[text_column].apply(clean_text)
    return df   # ✅ THIS LINE IS REQUIRED
