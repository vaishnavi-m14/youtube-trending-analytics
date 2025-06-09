import pandas as pd
import sqlite3

# STEP 1: Load CSV and save it as a SQL table
# ------------------------------------------
# Load the cleaned CSV file
df = pd.read_csv("cleaned_youtube_trending.csv")

# Connect to (or create) the SQLite database file
conn = sqlite3.connect("youtube_trending.db")

# Write the DataFrame to a new SQL table
df.to_sql("youtube_trending", conn, if_exists="replace", index=False)

print("✅ Table 'youtube_trending' created successfully in 'youtube_trending.db'.")

# STEP 2: Run SQL Query to get average views per category
# -------------------------------------------------------
query = """
SELECT 
    category_id,
    ROUND(AVG(views), 2) AS avg_views,
    COUNT(*) AS video_count
FROM 
    youtube_trending
GROUP BY 
    category_id
ORDER BY 
    avg_views DESC;
"""

# Execute the query and load results into a DataFrame
result = pd.read_sql_query(query, conn)

# Display results
print("\n📊 Average Views by Category:")
print(result)

# Optional: Save the result as a CSV file
result.to_csv("category_avg_views.csv", index=False)
print("\n✅ Results saved as 'category_avg_views.csv'.")

# Close the database connection
conn.close()
