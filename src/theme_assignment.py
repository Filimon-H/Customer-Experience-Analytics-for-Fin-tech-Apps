# src/theme_assignment.py


# theme_assignment.py

def assign_theme_to_review(text, bank, theme_dict):
    """
    Assign a theme to a review based on keyword matches from the theme dictionary.
    
    Parameters:
    - text (str): The cleaned review text.
    - bank (str): The bank associated with the review.
    - theme_dict (dict): Dictionary of bank -> themes -> keywords.

    Returns:
    - theme (str): The assigned theme.
    """
    themes = theme_dict.get(bank, {})
    for theme, keywords in themes.items():
        if any(keyword in text for keyword in keywords):
            return theme
    return "Other"


def label_reviews_with_theme(df, theme_dict):
    """
    Label each review with a theme based on the bank-specific keyword mapping.
    """
    def apply_theme(row):
        bank = row.get("bank", "")
        text = row.get("cleaned_review", "")
        keywords = theme_dict.get(bank, {})
        return assign_theme_to_review(text, keywords)

    df["theme"] = df.apply(apply_theme, axis=1)
    return df
