from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import schedule
import logging
import time

# Set up logging
logging.basicConfig(filename='scraper.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define app details for 3 banks
apps = [
    {
        "app_id": "com.dashen.dashensuperapp",
        "bank_name": "Dashen Bank"
    },
    {
        "app_id": "com.combanketh.mobilebanking",
        "bank_name": "Commercial Bank of Ethiopia"
    },
    {
        "app_id": "com.boa.boaMobileBanking",
        "bank_name": "Bank of Abyssinia"
    }
]

def scrape_play_store_reviews():
    logging.info("🔄 Fetching reviews for all apps...")

    for app in apps:
        try:
            logging.info(f"📱 Scraping: {app['bank_name']}")

            results, _ = reviews(
                app['app_id'],
                lang='en',
                country='us',
                sort=Sort.NEWEST,
                count=5000,
                filter_score_with=None
            )

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{app['bank_name'].replace(' ', '_')}_reviews_{timestamp}.csv"

            # Write to CSV
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
                writer.writeheader()

                for entry in results:
                    writer.writerow({
                        'review_text': entry['content'],
                        'rating': entry['score'],
                        'date': entry['at'].strftime('%Y-%m-%d'),
                        'bank_name': app['bank_name'],
                        'source': 'Google Play'
                    })

            logging.info(f"✅ Saved {len(results)} reviews to {filename}")

        except Exception as e:
            logging.error(f"❌ Error with {app['bank_name']}: {e}")

# Schedule to run daily at 1 AM (you can change this)
schedule.every().day.at("01:00").do(scrape_play_store_reviews)

# Optional: run once immediately for testing
scrape_play_store_reviews()

while True:
    schedule.run_pending()
    time.sleep(1)
