import pandas as pd
import os

def preprocess_reviews(input_path, output_path=None):
    """
    Cleans and preprocesses Google Play review data.
    
    Parameters:
    - input_path (str): Path to the raw CSV file.
    - output_path (str): Path to save the cleaned CSV (optional).
    
    Returns:
    - pd.DataFrame: The cleaned DataFrame.
    """
    try:
        # Load data
        df = pd.read_csv(input_path)

        # Drop duplicates
        df = df.drop_duplicates()

        # Drop rows with missing values in important fields
        df = df.dropna(subset=['review_text', 'rating', 'date'])

        # Convert 'date' column to datetime format
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        df = df.dropna(subset=['date'])  # Drop rows with invalid dates

        # Format date to YYYY-MM-DD
        df['date'] = df['date'].dt.strftime('%Y-%m-%d')

        # Rename columns to match final schema
        df = df.rename(columns={
            'review_text': 'review',
            'bank_name': 'bank'
        })

        # Keep only the required columns
        df = df[['review', 'rating', 'date', 'bank', 'source']]

        # Determine output file path
        if not output_path:
            folder, filename = os.path.split(input_path)
            name, ext = os.path.splitext(filename)
            output_path = os.path.join(folder, f"{name}_cleaned.csv")

        # Save cleaned data
        df.to_csv(output_path, index=False)
        print(f"✅ Cleaned data saved to: {output_path}")

        return df

    except Exception as e:
        print(f"❌ Error during preprocessing: {e}")
        return None

