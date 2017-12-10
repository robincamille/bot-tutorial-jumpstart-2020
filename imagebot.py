#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Tweet an Image Bot

# This bot tweets an image with a caption.
# It draws an image from an API and generates a random caption
# from a text file.

# Download a Project Gutenberg "Plain Text UTF-8" file,
# open it in Notepad, remove junk at beginning,
# and replace all double-linebreaks with single linebreaks.


# Housekeeping: do not edit
import tweepy
import requests
import time
import os
from random import randint
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


def random_integer():
    """ just generates a random integer """
    return randint(0, 200)


# We're going to make a request to an images API!
def image():
    """ make an API call, fetch an image and  save it to file """

    # There's a bunch of things that could possibly go wrong here,
    # so we're going to wrap the whole thing in at try block
    try:
        # Here's some parameters we're going to pass to the API
        url = 'https://api.qwant.com/api/search/images'
        parameters = {'q': 'pirates',
                      'count': '1',
                      'offset': str(random_integer())
                      }

        # We're going to add a header to trick the API into
        # thinking we're a browser
        headers = {'User-Agent': 'Chrome/62.0.3202.94'}

        # make the request! Include the parameters and the tricky
        # header we added!
        resp = requests.get(url, params=parameters, headers=headers)

        # We want the url for the image
        # So we'll get the json from the response
        resp_json = resp.json()

        # then we'll extract the bit we need (the url) and print it
        image_url = resp_json['data']['result']['items'][0]['media']
        print image_url

        # and make another request to get the image itself
        image_response = requests.get(image_url)

        # if this works, we'll save it to a file
        if image_response.status_code == 200:
            with open('downloadedimage.jpg', 'wb') as i:
                i.write(image_response.content)

        # if not, no big deal. We'll just move on
        else:
            print 'failed to download image. Passing.'
    except Exception as e:
        print 'Something went wrong. Passing.'
        print e
        pass


def caption():
    """ generate a caption and send the tweet """

    # Get the text that the bot will tweet
    filename = open('mariner.txt', 'r')
    tweet_text = filename.readlines()
    filename.close()

    # pick random line and tweet it with the image
    line = tweet_text[random_integer()]
    try:
        api.update_with_media('downloadedimage.jpg', status=line)
        print line

        # clean up after ourselves and delete the image file
        os.remove('downloadedimage.jpg')

    # If there's no image, for example because the image() function failed,
    # we'll just move on.
    except Exception as e:
        print e
        pass


# This loop runs the bot
while True:
    image()
    caption()
    time.sleep(30)

# To quit early: CTRL+C and wait a few seconds
