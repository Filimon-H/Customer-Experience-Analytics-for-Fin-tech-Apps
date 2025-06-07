# src/theme_grouping.py

from collections import defaultdict

# Define your manual theme groupings
#THEME_KEYWORDS = {
    #"Account Access Issues": ["login", "password", "verify", "verification", "access"],
   # "Transaction Performance": ["transfer", "delay", "error", "fail", "slow", "transaction"],
   # "User Interface & Experience": ["app", "UI", "interface", "friendly", "easy", "design", "responsive"],
   # "Customer Support": ["support", "help", "customer", "call", "contact", "respond"],
   # "Feature Requests": ["feature", "update", "add", "need", "functionality", "option"]
#}

THEME_KEYWORDS = {
    "User Interface & Experience": [
        "app", "UI", "interface", "friendly", "easy", "design", "responsive",
        "nice", "great", "excellent", "supper", "smooth", "simple", "user", "convenient"
    ],
    "Transaction Performance": [
        "transaction", "transfer", "delay", "slow", "fail", "working", "work", "processing", "network", "error"
    ],
    "Account Access Issues": [
        "login", "account", "password", "reset", "access", "verify", "verification"
    ],
    "Customer Support": [
        "support", "help", "service", "respond", "response", "call", "contact", "assistance", "thank", "fix"
    ],
    "Feature Requests & Innovation": [
        "feature", "update", "add", "need", "option", "functionality", "new", "step", "ahead", "digital"
    ],
    "General Sentiment & Feedback": [
        "good", "bad", "best", "worst", "like", "love", "wow", "ok", "thank", "better", "amazing", "great"
    ]
}

def group_keywords_into_themes(keywords_per_bank):
    """
    Map extracted keywords into themes for each bank.
    Returns a dictionary: bank -> {theme: [keywords]}
    """
    grouped = {}

    for bank, keywords in keywords_per_bank.items():
        themes = defaultdict(list)
        for word in keywords:
            matched = False
            for theme, words in THEME_KEYWORDS.items():
                if any(w in word.lower() for w in words):
                    themes[theme].append(word)
                    matched = True
                    break
            if not matched:
                themes["Other"].append(word)
        grouped[bank] = dict(themes)
    
    return grouped
