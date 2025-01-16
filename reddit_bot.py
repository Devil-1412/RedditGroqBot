import os
from groq import Groq
import time
import json
import praw
import requests
from datetime import datetime, timedelta

# --- Configuration ---
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_secret_code"
REDDIT_USERNAME = "your_username"
REDDIT_PASSWORD = "your_password"
REDDIT_USER_AGENT = "name_of_your_app"
GROQ_API_KEY = "your_groq_api_key"
POST_INTERVAL_HOURS = 6  # Post every 6 hours, can be changed

# --- Initialize Reddit API ---
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

client = Groq(api_key=GROQ_API_KEY)


def generate_content(prompt):
    """
    Generates content using the Groq AI API based on the provided prompt.

    Args:
        prompt (str): The prompt to guide Groq AI in generating content.

    Returns:
        tuple: A tuple containing the content (str) and title (str) of the post.
    """
    response = ""
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a Reddit user with actions- post and comment, based on user prompt produce an appropriate response in json structure everytime without json at start"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    print(response)
    response = json.loads(response)
    content = response.get("text", "")
    title = response.get("title", "Daily posts on AI")
    return content, title


def post_to_reddit(subreddit_name, content, title):
    """
    Posts the generated content to a specified subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to post to.
        content (str): The body text of the Reddit post.
        title (str): The title of the Reddit post.
    """
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title=title, selftext=content)
        print(f"Posted to r/{subreddit_name}")
    except Exception as e:
        print(f"Error posting to Reddit: {e}")


def schedule_posts():
    """
    Schedules posts to Reddit at regular intervals based on POST_INTERVAL_HOURS.

    Generates content using Groq AI and posts it to a specified subreddit, with optional comments on hot posts.
    """
    next_post_time = datetime.now()
    prompt = "Generate content for the post on AI development with 'title' and 'text' as the key fields"
    while True:
        if datetime.now() >= next_post_time:
            content, title = generate_content(prompt)
            if content:
                post_to_reddit("test", content, title)
                comment_on_posts("test")
            next_post_time = datetime.now() + timedelta(hours=POST_INTERVAL_HOURS)
            print(f"Next post scheduled at {next_post_time}")
        time.sleep(60)  # Check every minute


def comment_on_posts(subreddit_name):
    """
    Comments on the top posts of a specified subreddit.

    Args:
        subreddit_name (str): The name of the subreddit to comment on.
    """
    try:
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.hot(limit=5):
            prompt = f"Generate a comment based on the {post.title} with two key fields 'title' and 'text'"
            comment_text, title = generate_content(prompt)
            post.reply(comment_text)
            print(f"Commented on post: {post.title}")
    except Exception as e:
        print(f"Error commenting on posts: {e}")


# --- Main Execution ---
if __name__ == "__main__":
    schedule_posts()
