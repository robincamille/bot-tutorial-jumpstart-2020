#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 3

# This bot generates one variant of a poem using a mad-libs
# technique, replacing 3 words in the original with 3
# randomly-chosen words from 3 word lists.

# Original poem: This Is Just To Say by William Carlos Williams
# https://poets.org/poem/just-say

import requests
from random import randint
from credentials import *
import tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# gather some corpora from GitHub using requests; these are in JSON format
fruit_response = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/fruits.json')
adjectives_response = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/words/adjs.json')
colors_response = requests.get('https://raw.githubusercontent.com/dariusk/corpora/master/data/colors/crayola.json')

# Extract a Python-readable list from each response
fruits = fruit_response.json()['fruits']
adjectives = adjectives_response.json()['adjs']
colors = colors_response.json()['colors']
    
# Pick random numbers
# randint(0, len(xxx)-1) means choose random number between 0 and the length of the 
# word list named xxx 
fruit_num = randint(0, len(fruits)-1) 
adjectives_num = randint(0, len(adjectives)-1)
color_num = randint(0, len(colors)-1)

# Choose random items from each list using those random numbers
fruit_chosen = fruits[fruit_num].lower()
color_chosen = colors[color_num]['color'].lower()
adjective_chosen = adjectives[adjectives_num].lower()

# Fill in the blanks of the poem with the randomly chosen items
# \n means insert a line break
# \ at end of line just splits the line in the code, so that the code can be read more easily 

poem = 'This is just to say\n\n\
I have eaten\n\
the {0}s \n\
that were in\n\
the icebox \n\n\
and which\n\
you were probably\n\
saving\n\
for breakfast\n\n\
Forgive me\n\
they were delicious\n\
so {1} \n\
and so {2}' \
   .format(fruit_chosen, color_chosen, adjective_chosen)

api.update_status(status=poem)
print(poem)

## SAMPLE OUTPUT

## I have eaten
## the kumquats
## that were in
## the icebox
##
## and which
## you were probably
## saving
## for breakfast
##
## Forgive me
## they were delicious
## so unmellow yellow
## and so waterproof
