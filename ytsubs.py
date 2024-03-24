import matplotlib.pyplot as plt
import numpy as np

def plot_subscriber_count(channel_id, subscriber_count):
    """
    Plot subscriber count for a YouTube channel.

    Args:
    - channel_id: YouTube channel ID
    - subscriber_count: List of subscriber counts over time
    """

    # Generate x-axis values (time)
    x = np.arange(len(subscriber_count))

    plt.plot(x, subscriber_count, color='blue', marker='o', linestyle='-', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel('Subscriber Count')
    plt.title(f'Subscriber Count for YouTube Channel {channel_id}')
    plt.grid(True)
    
    # Set the limits of the y-axis to zoom in
    plt.ylim(bottom=0, top=max(subscriber_count) * 1.2)  # Increase top limit by 20%

    plt.savefig('subscriber_count_graph.png')  # Save the graph as an image file
    plt.close()

# Example usage
if __name__ == "__main__":
    # YouTube channel ID
    channel_id = 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'  # Replace with your YouTube channel ID

    # Sample subscriber count data (replace with actual data)
    subscriber_count = [1000, 1200, 1500, 1800, 2000, 2500]
 
    # Plot subscriber count
    plot_subscriber_count(channel_id, subscriber_count)
