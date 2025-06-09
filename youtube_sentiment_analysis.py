import pandas as pd
from textblob import TextBlob

# Load the cleaned dataset
df = pd.read_csv("cleaned_youtube_trending.csv")

# Convert date columns to datetime
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce')
df['publish_date'] = pd.to_datetime(df['publish_date'], errors='coerce')

# Remove missing values and duplicates
df.dropna(inplace=True)
df.drop_duplicates(subset='video_id', keep='first', inplace=True)

# Apply sentiment score using TextBlob
df['sentiment_score'] = df['title'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Function to label sentiment
def get_sentiment_label(score):
    if score > 0.1:
        return 'Positive'
    elif score < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment label
df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

# Preview result (optional)
print(df[['title', 'sentiment_score', 'sentiment_label']].head())

# Save result to new CSV for Tableau
df.to_csv("cleaned_youtube_sentiment.csv", index=False)
