# 📊 YouTube Trending Video Analytics

## 🎯 Objective  
Uncover patterns in trending YouTube videos across regions by analyzing content categories, viewer sentiments, and engagement metrics.

## 🧰 Tools Used  
- 🐍 Python (Pandas, TextBlob, Matplotlib, Seaborn)  
- 💾 SQL (SQLite / MySQL)  
- 📈 Tableau (Desktop or Public)

  ## 📂 Dataset
We used the **YouTube Trending Video Dataset** available on Kaggle:  
🔗 [YouTube Trending Video Dataset – Kaggle](https://www.kaggle.com/datasets/datasnaek/youtube-new)


## 🔍 Project Workflow  
1. 🧹 **Data Cleaning** – Remove duplicates, fix date formats, handle missing data  
2. 💬 **Sentiment Analysis** – Analyze video titles using TextBlob  
3. 📊 **SQL Queries** – Rank video categories by average views  
4. 📉 **Dashboard Creation** – Build visualizations in Tableau  
5. 📝 **Final Report** – Present key findings using data storytelling


## 🚀 How to Use  
- ⚙️ Run `youtube_sentiment_analysis.ipynb` to clean and analyze the data  
- 📂 Import the resulting CSV into your SQL environment to run queries  
- 📊 Open Tableau and connect `cleaned_youtube_sentiment.csv` to design dashboards  
- 📑 Review insights in `Report.pdf`  

## ✅ Output Highlights  
- Most trending categories (by average views)  
- Sentiment distribution (Positive, Neutral, Negative)  
- Region-wise comparisons and video behavior
