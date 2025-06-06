# Customer-Experience-Analytics-for-Fin-tech-Apps
Data Engineering Challenge: Scraping, Analysing, and Visualising Google Play Store Reviews
# 📱 Customer Experience Analytics for Fintech Apps

**Week 2 Data Engineering Challenge – Omega Consultancy**  
📅 **Date**: 04 June – 10 June 2025

---

## 🔍 Project Overview

This project analyzes customer experiences with mobile banking apps in Ethiopia by collecting and cleaning user reviews from the Google Play Store. The focus is on three major banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The insights will help improve app features, user satisfaction, and customer support strategies.

---

## 🎯 Business Objective

Omega Consultancy is supporting banks in improving customer retention through data insights.  
As part of the consulting team, our goals for Task 1 were to:

- Scrape 400+ reviews per bank from the Play Store
- Clean and normalize the review data
- Save the cleaned data in a structured format for further analysis

---

## ⚙️ Methodology – Task 1: Data Collection & Preprocessing

### ✅ 1. Data Scraping
- Used the `google-play-scraper` Python library
- Collected review text, star rating, date, app name, and source
- Saved raw data into separate `.csv` files for each bank

### ✅ 2. Data Preprocessing
- Removed duplicate reviews and entries with missing values
- Normalized dates into `YYYY-MM-DD` format
- Saved cleaned data to new `.csv` files for each bank

### ✅ 3. Validation & Quality Check
- Ensured each cleaned dataset had **≥ 400 reviews**
- Verified **<5% of data was removed** during preprocessing

---

## 📁 Project Structure