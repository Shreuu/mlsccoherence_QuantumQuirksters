from googleapiclient.discovery import build
from textblob import TextBlob
import matplotlib.pyplot as plt

# Set up YouTube Data API service
api_key = 'AIzaSyD5Lv7oUtzvyn71xKiWtm-zw8Gb7CtkoHo'  # Replace with your YouTube Data API key
youtube = build('youtube', 'v3', developerKey=api_key)

def fetch_top_videos(query, max_results=5):
    """
    Fetch the top videos on YouTube based on a search query.

    Args:
    - query: The search query to find top videos.
    - max_results: Maximum number of videos to fetch (default is 5).

    Returns:
    - video_ids: List of video IDs of the top videos.
    """
    video_ids = []
    request = youtube.search().list(
        q=query,
        part='id',
        type='video',
        maxResults=max_results,
        order='viewCount'
    )
    response = request.execute()
    for item in response['items']:
        video_ids.append(item['id']['videoId'])
    return video_ids

def fetch_video_comments(video_id, max_results=100):
    """
    Fetch comments of a YouTube video.

    Args:
    - video_id: ID of the YouTube video.
    - max_results: Maximum number of comments to fetch (default is 100).

    Returns:
    - comments: List of comments.
    """
    comments = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=max_results
    )
    response = request.execute()
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)
    return comments

def analyze_sentiment(text):
    """
    Perform sentiment analysis on the given text.

    Args:
    - text: The text to analyze.

    Returns:
    - sentiment: The sentiment of the text (polarity).
    """
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

def classify_sentiment(sentiment):
    """
    Classify sentiment into positive, negative, or neutral.

    Args:
    - sentiment: Sentiment score.

    Returns:
    - category: Sentiment category (positive, negative, or neutral).
    """
    if sentiment > 0.2:
        return 'positive'
    elif sentiment < -0.2:
        return 'negative'
    else:
        return 'neutral'

def plot_sentiment_comparison(sentiments):
    """
    Plot sentiment comparison of comments from top videos on YouTube.

    Args:
    - sentiments: List of sentiment categories for each video.
    """
    categories = ['positive', 'negative', 'neutral']
    counts = {category: [video_sentiments.count(category) for video_sentiments in sentiments] for category in categories}

    bar_width = 0.3
    x_values = range(len(sentiments))
    for i, category in enumerate(categories):
        plt.bar([x + i * bar_width for x in x_values], counts[category], bar_width, label=category)

    plt.xlabel('Top Videos')
    plt.ylabel('Count')
    plt.title('Sentiment Comparison of Top Videos on YouTube')
    plt.xticks([x + bar_width for x in x_values], [f'Video {i+1}' for i in x_values])
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    search_query = 'music'  # Search query to find top videos
    top_videos = fetch_top_videos(search_query)
    sentiments = []
    for video_id in top_videos:
        comments = fetch_video_comments(video_id)
        video_sentiments = [classify_sentiment(analyze_sentiment(comment)) for comment in comments]
        sentiments.append(video_sentiments)
    plot_sentiment_comparison(sentiments)
