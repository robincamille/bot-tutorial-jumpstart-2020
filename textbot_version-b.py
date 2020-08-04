#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 2, version B

# This bot tweets a text file line by line, waiting a
# given period of time between tweets.

# Version B changes:
# This script uses a double-whammy of if/else statements
# so your bot only tweets if the line is not blank.
# Also, rather than stopping when it gets an error message like
# "Status is a duplicate," it will just skip the error and move on.

# Try this with another .txt file!
# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in a plain text editor and remove junk at beginning.

# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet
filename = open('twain.txt','r') 
tweet_text = filename.readlines() 
filename.close()

# loop through the tweet_list
for line in tweet_text: 
    if len(line) > 0: # Do the following if the line is not blank
        try: # Attempt the following
            api.update_status(status=line)
            print("Tweeted that line!")
        except: # If you get an error, do the following
            print("Unable to tweet that line")
        time.sleep(2) # Sleep for 2 seconds
    else:
        pass # If the line is blank, ignore it and move on with our lives

print("All done!")

# To quit early: CTRL+C and wait a few seconds
