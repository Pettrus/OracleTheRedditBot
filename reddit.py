import praw
import praw.models
from dotenv import load_dotenv
import os

load_dotenv()

reddit = praw.Reddit(client_id=os.getenv("CLIENT_ID"),
                     client_secret=os.getenv("CLIENT_SECRET"),
                     username=os.getenv("USERNAMEREDDIT"),
                     password=os.getenv("PASSWORD"),
                     user_agent=os.getenv("USER_AGENT"))

def hotQuestions():
    return reddit.subreddit('askreddit').hot(limit=9)

def moreComments():
    return praw.models.MoreComments