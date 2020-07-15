# Twitter bot tutorial: Jumpstart Program 2020 edition

*See original repo: https://github.com/robincamille/bot-tutorial*

This tutorial and its updated materials were originally put together by Robin Davis (@robincamille) and Mark Eaton (github.com/MarkEEaton) for a pre-conference workshop at [Code4Lib 2018](http://2018.code4lib.org/).

See also: Davis, Robin, and Mark Eaton. [Make a Twitter Bot in Python: Iterative Code Examples](http://jitp.commons.gc.cuny.edu/make-a-twitter-bot-in-python-iterative-code-examples/). *Journal of Interactive Technology and Pedagogy* (Blueprints section).  April 2016. (Verbose write-up featuring [code from a previous version](https://github.com/robincamille/bot-tutorial) of this workshop.)

Written in Python 3.

**Required libraries:** tweepy 3.5, requests, time, os, random

## Installation Specifications

For this workshop, you will need to follow the Jumpstart Program install fest instructions to set up Anaconda (which will install python for you and the required libraries listed above), VSCode, and a Twitter developer account.

## Get credentials from your Twitter account 

1. Go to http://apps.twitter.com and create a new app
 - This info isn't public so it can be messy 
 - Go to `Keys and Access Tokens`
 - `Create my access token`

2. Copy Consumer Key/Secret and Access Key/Secret to **credentials.template** and save as a new file named **credentials.py**

3. (Optional) Follow (account TBD), which will follow & retweet bots made in this workshop

## Running Code

Once you have your environment set up, you can fork this repository to get started and then clone it to your local machine. 

1. Fork this repository by clicking the button labeled 'fork' in the top right corner of this window. 

2. Clone the repository to your local machine.
- Copy the repository url from your browser. 
- In your terminal [mac] or command line [windows], navigate to the repository where you  want this repository to live (your Desktop, for example), and then run the following command to clone the repository to that location: `git clone [repository url]`

3. Navigate into that repository with the command `cd bot-tutorial-jumpstart`

To test things out and get familiar with how we will be running code throughout the workshop, follow these steps:

1. Using your finder or search box, find the folder on your desktop. Open the folder and open the file test.py in VS Code.
2. To run the code, click the green triangle in the upper right corner of the VS Code window.  (*link to marked up screenshot*) 

You should see “Hello, there!” printed in the Terminal part of this window (the lower half).  (*link to marked up screenshot*)  

## Basic bot: listbot.py

This script is a basic Twitter bot. It will tweet three things from a **list** inside the script.

1. Go to the bot-tutorial-jumpstart folder. Click on `listbot.py` to see the code

2. Take a look at the script; Robin and Tori will talk about what it's doing

3. Clicking `Run` will run the bot. A console will appear at the bottom of the screen with the output

*Change it up!*
- In `tweetlist`, add new things for your bot to tweet
- Increase/decrease time between tweets in `time.sleep(15)` (15 is the number of seconds) 

## Intermediate bot: textbot.py

This script sends out five tweets from the first five lines of an external .txt file

1. Go to the bot-tutorial-jumpstart folder. Click on `textbot.py`

2. Also look at `twain.txt` to see the text

3. Take a look at both files; Robin and Tori will talk about what the script is doing

4. Select `Run`

*Change it up!*
 - Go to http://gutenberg.org and choose a different text for your bot to tweet. Pick the "Plain Text UTF-8" option when selecting a text format.
   - On PythonAnywhere, you can select `New Empty File`. This will only work if you've entered a filename. Copy and paste your gutenberg.org text (or any text of your choosing) into this blank file
   - Remove junk at the beginning (and the end) of the file. Save the file
   - Replace double linebreaks with single linebreaks. If your file is very short you can maybe do this manually.
   - For longer files you can click on `Open bash console here` and type: `cd bot-tutorial-jumpstart` then `grep . filename > newfilename`. Open up the new file to make sure that it worked.
   - If you're on a Windows machine, the grep command above might not work as expected, because Windows handles line endings differently than Mac or linux systems. If you're having this problem, replace the grep command above with `grep -v "^[[:space:]]*$" filename > newfilename`
   - In textbot.py, replace `twain.txt` with the `newfilename` 
 - Make the bot send more or fewer tweets, or change which lines, by editing the numbers in `for line in tweettext[0:5]`. 
   - `[0:5]` means from the first thing up to (but not including) the fifth thing
 
 
## Advanced bot: poembot.py

This script treats the poem *This Is Just To Say* (William Carlos Williams) as a mad-lib, filling in 3 blanks from 3 data sources: JSON files from @dariusk's [collection of corpora](https://github.com/dariusk/corpora). 

*Change it up!*
- Choose different [word lists](https://github.com/dariusk/corpora). Make sure to change the URLs in lines ``16-19`` and the list name in lines ``22-25``.
- Choose a different piece of text to make into a mad lib. 

