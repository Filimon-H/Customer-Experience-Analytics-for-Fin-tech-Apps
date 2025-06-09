import oracledb
import pandas as pd

# Load CSV
df = pd.read_csv("C:/Users/User/Desktop/Week_2/Customer-Experience-Analytics-for-Fin-tech-Apps/data/merged_comparison_review.csv")

# Connect to Oracle DB
connection = oracledb.connect(
    user="Bankadm",
    password="Bankadm123",  
    dsn="localhost/XEPDB1"
)
cursor = connection.cursor()

# Fetch bank_id mappings from banks table
cursor.execute("SELECT bank_id, bank_name FROM banks")
bank_map = {name.lower().strip(): bank_id for bank_id, name in cursor.fetchall()}

# Insert reviews
for _, row in df.iterrows():
    bank_name = row['bank'].lower().strip()
    bank_id = bank_map.get(bank_name)

    if bank_id is None:
        print(f"⚠️ Skipping unknown bank: '{row['bank']}'")
        continue

    cursor.execute("""
        INSERT INTO reviews (
            bank_id, review_text, theme,
            sentiment_score_distilbert, sentiment_label_distilbert,
            sentiment_score_vader, sentiment_label_vader,
            sentiment_score_textblob, sentiment_label_textblob
        ) VALUES (
            :bank_id, :review_text, :theme,
            :s_distilbert, :l_distilbert,
            :s_vader, :l_vader,
            :s_textblob, :l_textblob
        )
    """, {
        'bank_id': bank_id,
        'review_text': row['review'],
        'theme': row['theme'],
        's_distilbert': row['sentiment_score_distilbert'],
        'l_distilbert': row['sentiment_label_distilbert'],
        's_vader': row['sentiment_score_vader'],
        'l_vader': row['sentiment_label_vader'],
        's_textblob': row['sentiment_score_textblob'],
        'l_textblob': row['sentiment_label_textblob']
    })

# Finalize
connection.commit()
cursor.close()
connection.close()

print("✅ All reviews inserted into the Oracle DB.")
