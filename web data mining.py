import requests
from bs4 import BeautifulSoup

# Example social media platform URL
url = "https://twitter.com/search?q=hp%20printer&src=typed_query"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the posts on the page
posts = soup.find_all("div", {"class": "tweet"})

# Extract the text content and metadata of each post and store it in a dictionary
post_data = []
for post in posts:
    data = {}
    data["text"] = post.find("div", {"class": "tweet-text"}).text
    data["user"] = post.find("span", {"class": "username"}).text
    data["timestamp"] = post.find("span", {"class": "timestamp"}).text
    post_data.append(data)

# Process the collected post data as required (e.g., perform NLP, sentiment analysis, etc.)
for data in post_data:
    # Perform NLP, sentiment analysis, etc. on each post data
    ...
