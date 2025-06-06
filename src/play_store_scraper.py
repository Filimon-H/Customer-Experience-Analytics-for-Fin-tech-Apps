# Import required modules
from google_play_scraper import Sort, reviews  # For scraping Google Play reviews
import csv  # To write reviews to CSV files
from datetime import datetime  # To add a timestamp to output filenames
import schedule  # To schedule the scraping task
import logging  # To record the scraping progress and errors in a log file
import time  # For sleeping in the loop

# Set up logging to track activity and errors in a log file
logging.basicConfig(
    filename='scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

#  Define the list of apps you want to scrape (3 Ethiopian bank apps)
apps = [
    {
        "app_id": "com.dashen.dashensuperapp",  # Dashen Bank app ID
        "bank_name": "Dashen Bank"  # Name to use in CSV and logs
    },
    {
        "app_id": "com.combanketh.mobilebanking",  # CBE app ID
        "bank_name": "Commercial Bank of Ethiopia"
    },
    {
        "app_id": "com.boa.boaMobileBanking",  # BOA app ID
        "bank_name": "Bank of Abyssinia"
    }
]

#  Function to scrape reviews for all listed apps
def scrape_play_store_reviews():
    logging.info("🔄 Fetching reviews for all apps...")  # Log start

    for app in apps:
        try:
            logging.info(f"📱 Scraping: {app['bank_name']}")  # Log which app is being scraped

            # Use google-play-scraper to get up to 5000 recent reviews
            results, _ = reviews(
                app['app_id'],         # The app’s ID
                lang='en',             # Language: English
                country='us',          # Country: US
                sort=Sort.NEWEST,      # Sort by newest reviews
                count=5000,            # Max reviews to fetch
                filter_score_with=None # No filter, include all ratings
            )

            #  Create a unique filename using the bank name and timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{app['bank_name'].replace(' ', '_')}_reviews_{timestamp}.csv"

            #  Open CSV file for writing the reviews
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                # Define the column headers
                writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
                writer.writeheader()  # Write the header row

                # Loop through all fetched reviews and write each to the CSV
                for entry in results:
                    writer.writerow({
                        'review_text': entry['content'],  # The text of the review
                        'rating': entry['score'],         # The star rating (1–5)
                        'date': entry['at'].strftime('%Y-%m-%d'),  # Format date to YYYY-MM-DD
                        'bank_name': app['bank_name'],    # Name of the bank
                        'source': 'Google Play'           # Source of the review
                    })

            logging.info(f"✅ Saved {len(results)} reviews to {filename}")  # Log success

        except Exception as e:
            # If an error occurs, log it with the bank name
            logging.error(f"❌ Error with {app['bank_name']}: {e}")

#  Schedule the scraping to run daily at 1:00 AM (you can change this time)
schedule.every().day.at("01:00").do(scrape_play_store_reviews)

# Optional: Run the scraping once right now (useful for testing)
scrape_play_store_reviews()

# ⏲ Start an infinite loop to keep the scheduler running
while True:
    schedule.run_pending()  # Check if a scheduled task should run
    time.sleep(1)           # Sleep 1 second to avoid high CPU usage
