#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tweets one variant of This Is Just To Say by William Carlos Williams
# original: https://www.poetryfoundation.org/poems/56159/this-is-just-to-say

import json, io, time, urllib2
from random import randint
from credentials import *
##import tweepy
##auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
##auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
##api = tweepy.API(auth)

fruit_file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/foods/fruits.json')
fruit_list = fruit_file.read()

rooms_file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/architecture/rooms.json')
rooms_list = rooms_file.read()

adjectives_file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/words/adjs.json')
adjectives_list = adjectives_file.read()

colors_file = urllib2.urlopen('https://raw.githubusercontent.com/dariusk/corpora/master/data/colors/crayola.json')
colors_list = colors_file.read()


# Create Python-readable lists of items in JSON files
fruits = json.loads(fruit_list)['fruits']
rooms = json.loads(rooms_list)['rooms']
adjectives = json.loads(adjectives_list)['adjs']
colors = json.loads(colors_list)['colors']

    
# Pick random numbers
fruit_num = randint(0, len(fruits)-1)
room_num = randint(0, len(rooms)-1)
adjectives_num = randint(0, len(adjectives)-1)
color_num = randint(0, len(colors)-1)

# Choose random items from each list using random numbers
fruit_chosen = fruits[fruit_num].lower() #should be pluralized here but pluralizing is hard
room_chosen = rooms[room_num].lower()
color_chosen = colors[color_num]['color'].lower()
adjective_chosen = adjectives[adjectives_num].lower()

# Fill in the blanks of the poem
poem = 'I have eaten\nthe %ss\nthat were in\nthe %s\n\nand which\nyou were probably\nsaving\nfor breakfast\n\nForgive me\nthey were delicious\nso %s\nand so %s' \
       % (fruit_chosen, room_chosen, color_chosen, adjective_chosen)

#api.update_status(poem)
print poem

## SAMPLE OUTPUT

##I have eaten
##the apricots
##that were in
##the storm cellar
##
##and which
##you were probably
##saving
##for breakfast
##
##Forgive me
##they were delicious
##so black
##and so hopeless
