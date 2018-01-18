# Twitter bot tutorial: Code4Lib 2018 edition

**Under construction: Files may not work! See original repo: https://github.com/robincamille/bot-tutorial**

This tutorial and its materials are put together by Robin Davis (@robincamille) and Mark Eaton (github.com/MarkEEaton) for a pre-conference workshop at [Code4Lib 2018](http://2018.code4lib.org/). 

See also: Davis, Robin, and Mark Eaton. [Make a Twitter Bot in Python: Iterative Code Examples](http://jitp.commons.gc.cuny.edu/make-a-twitter-bot-in-python-iterative-code-examples/). *Journal of Interactive Technology and Pedagogy* (Blueprints section).  April 2016. (Verbose write-up featuring [code from a previous version](https://github.com/robincamille/bot-tutorial) of this workshop.)

**Required libraries:** tweepy 3.5, requests, time, os, random

## Create an account on PythonAnywhere

1. Go to https://pythonanywhere.com and create an account by clicking on `Start running Python online in less than a minute`
 - Select `Create a beginner account` and fill out your details
 - Select `Account` on the top right
 - Select `Teacher` and enter `robincamille` or `b7jl` so that we can add the sample code to your account
 - Or if you prefer to use git, you can `git clone https://github.com/robincamille/bot-tutorial-code4lib.git`

## Create a Twitter account for your bot

1. Go to http://twitter.com and sign up for a new account of your choosing
 - Be sure to include your mobile number (required for using the API) 
 - Email address must be unique to Twitter users; try adding random periods in your Gmail address, if you have one

2. Go to http://apps.twitter.com and create a new app
 - This info isn't public so it can be messy 
 - Go to `Keys and Access Tokens`
 - `Create my access token`

3. Copy Consumer Key/Secret and Access Key/Secret to **credentials.py**

## Basic bot: mybot.py

This script is a basic Twitter bot. It will tweet three things from a **list** inside the script

1. Go to the bot-tutorial-code4lib folder. Click on `mybot.py` to see the code

2. Take a look at the script; Robin and Mark will talk about what it's doing

3. Clicking `Run` will run the bot. A console will appear at the bottom of the screen with the output

*Change it up!*
- In **tweetlist**, add new things for your bot to tweet
- Increase/decrease time between tweets in **time.sleep(15)** (15 is the number of seconds) 

## Intermediate bot: mybot2.py

This script sends out five tweets from the first five lines of an external .txt file

1. Go to the bot-tutorial-code4lib folder. Click on `mybot2.py`

2. Also look at `twain.txt` to see the text

3. Take a look at both files; Robin and Mark will talk about what the script is doing

4. Select `Run`

*Change it up!*
 - Go to http://gutenberg.org and choose a different text for your bot to tweet
 - On PythonAnywhere, you can select `New Empty File`. This will only work if you've entered a filename. Copy and paste your gutenberg.org text into this blank file
 - Remove junk at the beginning (and the end) of the file. Save the file
 - Replace double linebreaks with single linebreaks. If your file is very short you can maybe do this manually. For longer files you can click on `Open bash console here` and type: `cd bot-tutorial-code4lib` then `grep . filename > newfilename`
 - In mybot2.py, replace `twain.txt` with the newfilename 
- Make the bot send more or fewer tweets, or change which lines, by editing the numbers in **for line in tweettext[0:5]**. 
 - [0:5] means from the first thing up to (but not including) the fifth thing
 
## Advanced bot: plumpoem.py

This script treats the poem *This Is Just To Say* (William Carlos Williams) as a mad-lib, filling in four blanks from four data sources: JSON files from @dariusk's [collection of corpora](https://github.com/dariusk/corpora). 

## Advanced bot: respondingbot.py

This script tweets a random line from a .txt file whenever @ocertat tweets


## Advanced bot: mashup_markov

This script (markovmaker.py) uses a Markov chain to create new sentences from another text (twain.txt is included), and tweets them


## Advanced bot: imagebot.py

This bot makes a call to an images API, downloads an image, then tweets it with a caption drawn from a .txt file
