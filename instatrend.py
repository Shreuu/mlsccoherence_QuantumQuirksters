import instaloader
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Initialize Instaloader
L = instaloader.Instaloader()

def get_followers(username):
    """
    Get followers count for a given Instagram username.

    Args:
    - username: Instagram username

    Returns:
    - followers: List of follower counts over time
    """

    profile = instaloader.Profile.from_username(L.context, username)
    follower_count = []

    for post in profile.get_posts():
        follower_count.append(post.owner_profile.followers)

    return follower_count

def trend_analysis(y):
    """
    Performs trend analysis using linear regression.

    Args:
    - y: Dependent variable (follower counts)

    Returns:
    - slope: Slope of the trend line
    - intercept: Intercept of the trend line
    - r_value: Correlation coefficient
    - p_value: Two-sided p-value for the hypothesis test
    - std_err: Standard error of the estimated gradient
    """

    # Independent variable (time)
    x = np.arange(len(y))

    # Perform linear regression
    slope, intercept, r_value, p_value, std_err = linregress(x, y)

    return slope, intercept, r_value, p_value, std_err

def plot_trend(y, slope, intercept):
    """
    Plots the follower counts along with the trend line.

    Args:
    - y: Follower counts
    - slope: Slope of the trend line
    - intercept: Intercept of the trend line
    """

    plt.plot(y, color='b', label='Follower Counts')
    plt.plot(slope*np.arange(len(y)) + intercept, color='r', label='Trend Line')

    # Highlight upward and downward trends
    for i in range(len(y) - 1):
        if y[i+1] > y[i]:
            plt.plot([i, i+1], [y[i], y[i+1]], color='g')  # Upward trend
        elif y[i+1] < y[i]:
            plt.plot([i, i+1], [y[i], y[i+1]], color='r')  # Downward trend

    plt.xlabel('Time')
    plt.ylabel('Follower Count')
    plt.title('Instagram Follower Trend Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Instagram username
    username = 'kartik.rathodd'  # Replace with your Instagram username
    # Get follower counts
    follower_counts = get_followers(username)

    if len(follower_counts) > 0:
        # Perform trend analysis
        slope, intercept, r_value, p_value, std_err = trend_analysis(follower_counts)

        # Print results
        print("Slope:", slope)
        print("Intercept:", intercept)
        print("R-squared:", r_value**2)
        print("P-value:", p_value)

        # Plot trend line
        plot_trend(follower_counts, slope, intercept)
    else:
        print("No follower counts found.")
