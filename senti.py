# Import necessary libraries
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
    - video_data: List of dictionaries containing video data.
    """
    video_data = []
    request = youtube.search().list(
        q=query,
        part='id,snippet',  # Include snippet in the request to ensure the 'snippet' key is present
        type='video',
        maxResults=max_results,
        order='viewCount'
    )
    response = request.execute()
    for item in response.get('items', []):  # Check if 'items' key exists
        video_id = item['id']['videoId']
        video_title = item['snippet']['title']
        video_data.append({'video_id': video_id, 'title': video_title})
    return video_data

def fetch_video_statistics(video_id):
    """
    Fetch statistics of a YouTube video.

    Args:
    - video_id: ID of the YouTube video.

    Returns:
    - statistics: Dictionary containing video statistics.
    """
    request = youtube.videos().list(
        part='statistics',
        id=video_id
    )
    response = request.execute()
    items = response.get('items', [])
    if items:
        statistics = items[0]['statistics']
        return statistics
    else:
        print("No statistics found for the given video ID.")
        return {}

# Example usage
if __name__ == "__main__":
    search_query = 'music'  # Search query to find top videos
    top_videos = fetch_top_videos(search_query)
    video_statistics = []
    for video in top_videos:
        statistics = fetch_video_statistics(video['video_id'])
        if statistics:
            video_statistics.append({
                'title': video['title'],
                'views': int(statistics.get('viewCount', 0)),
                'likes': int(statistics.get('likeCount', 0)),
                'comments': int(statistics.get('commentCount', 0))
            })

    # Plot line graph
    categories = ['views', 'likes', 'comments']
    plt.figure(figsize=(10, 6))
    for category in categories:
        data = [video[category] for video in video_statistics]
        plt.plot([video['title'] for video in video_statistics], data, marker='o', label=category)

    plt.title('Comparison of Top Videos on YouTube')
    plt.xlabel('Videos')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
