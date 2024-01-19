# import all thr modules
import os

from selenium import webdriver
from instafollower import InstaFollower




SIMILAR_ACCOUNTS = "charlie_billionaire"
USERNAME = os.environ["username"]
PASSWORD = os.environ["password"]



insta = InstaFollower()
insta.login(USER=USERNAME,PASS=PASSWORD)
insta.findfollowers(to_search=SIMILAR_ACCOUNTS)
insta.follow()