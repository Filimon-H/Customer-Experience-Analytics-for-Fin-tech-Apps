# 📱 Ethiopian Banking App Reviews – Sentiment & Thematic Analysis

## 🧠 Project Overview
This project analyzes user reviews from the Google Play Store for three major Ethiopian banking apps:  
- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

We apply **NLP and ML techniques** to uncover key customer pain points and satisfaction drivers. The goal is to extract **sentiment insights** and **thematic trends** that banks can use to improve their mobile services.

---

## 🔍 Business Objective

- **Sentiment Analysis**: Quantify the emotional tone (positive/negative/neutral) in each review.
- **Thematic Analysis**: Identify recurring topics such as login issues, transaction problems, and UI/UX complaints.
- **Insight Generation**: Derive actionable feedback per bank and compare experiences across institutions.

---

## 📂 Project Structure

├── data/
│ ├── raw/ # Raw scraped reviews
│ ├── processed/ # Cleaned datasets
├── notebooks/
│ ├── sentiment_analysis.ipynb
│ ├── theme_extraction.ipynb
├── src/
│ ├── preprocessing.py # Data cleaning script
│ ├── sentiment_scoring.py # DistilBERT sentiment scoring
│ ├── theme_extraction.py # TF-IDF or spaCy keyword extraction
│ ├── theme_grouping.py # Rule-based theme grouping
│ ├── theme_assignment.py # Assign theme(s) per review
├── outputs/
│ ├── BOA_reviews_with_sentiment_DistilBERT.csv
│ ├── CBE_reviews_with_sentiment_DistilBERT.csv
│ ├── Dashen_Bank_reviews_with_sentiment_DistilBERT.csv
├── .gitignore
├── requirements.txt
├── README.md

markdown
Copy
Edit

---

## ✅ Tasks Completed

### Task 1: Data Collection & Preprocessing
- Scraped **400+ reviews** per bank using `google-play-scraper`
- Normalized columns: `review`, `rating`, `date`, `bank`, `source`
- Cleaned datasets saved to `/data/processed/`

### Task 2: Sentiment & Thematic Analysis
- Used `distilbert-base-uncased-finetuned-sst-2-english` to assign sentiment labels and scores
- Extracted top keywords using **spaCy + TF-IDF**
- Grouped into 3–5 themes per bank:
  - Account Access Issues
  - Transaction Reliability
  - UI/UX Experience
  - Customer Support
  - Feature Requests
- Merged sentiment and theme data into final CSVs

---

## 📊 Key Results
- **1,200+ reviews** analyzed with **<5% missing**
- **Sentiment distribution** per bank and rating
- **Top themes** highlight usability, login, and performance concerns
- Clean GitHub repo with semantic commits and modular scripts

---

## 🛠️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/ethiopian-banking-review-analysis.git
cd ethiopian-banking-review-analysis
Create virtual environment

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run preprocessing

bash
Copy
Edit
python src/preprocessing.py
Run sentiment analysis

bash
Copy
Edit
python src/sentiment_scoring.py
Run thematic analysis

bash
Copy
Edit
python src/theme_extraction.py
python src/theme_grouping.py
python src/theme_assignment.py