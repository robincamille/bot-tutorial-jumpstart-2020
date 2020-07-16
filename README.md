# Twitter bot tutorial: Jumpstart Program 2020 edition

*See original repo: https://github.com/robincamille/bot-tutorial*

Let's make a bot!! These instructions are written for participants in the Jumpstart Program.

**Required libraries:** tweepy 3.5, requests, time, os, random. Written in Python 3. 

---

## Installation Specifications

For this workshop, you will need to follow the Jumpstart Program install-fest instructions to set up Anaconda (which will install Python for you and the required libraries listed above), VSCode, and a Twitter developer account.

## Get credentials from your Twitter account 

1. Go to http://apps.twitter.com and create a new app
 - This info isn't public so your app name/descrition can be messy 
 - Go to `Keys and Access Tokens`
 - `Create my access token`

2. Copy Consumer Key/Secret and Access Key/Secret to **credentials.template** 

3. Save that file as a new file named **credentials.py**

## Running Code

Once you have your environment set up, you can fork this repository to get started and then clone it to your local machine. 

1. Fork this repository by clicking the button labeled 'fork' in the top right corner of this window. 

2. Clone the repository to your local machine.
- Copy the repository url from your browser. 
- In your terminal [mac] or command line [windows], navigate to the repository where you  want this repository to live (your Desktop, for example), and then run the following command to clone the repository to that location: `git clone [repository url]`

3. Navigate into that repository with the command `cd bot-tutorial-jumpstart`

To test things out and get familiar with how we will be running code throughout the workshop, follow these steps:

1. Using your finder or search box, find the folder on your desktop. Open the folder and open the file test.py in VS Code.
2. To run the code, click the green triangle in the upper right corner of the VS Code window. 
3. Look for “Hello, there!” printed in the Terminal part of this window (the lower half). 

[View an annotated screenshot of how to edit and run Python code in VS Code](http://robincamille.com/ncsu/vscode_screenshot_python.png)

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
- New text source
  - Go to http://gutenberg.org and choose a different text for your bot to tweet. Pick the "Plain Text UTF-8" option when selecting a text format.
  - Open a text editor. Copy and paste your gutenberg.org text (or any text of your choosing) into this blank file
  - Remove junk at the beginning (and the end) of the file. Save the file as a .txt
  - Replace double linebreaks with single linebreaks. If your file is very short you can maybe do this manually. If the file is very long, you can use advanced find/replace
  - In textbot.py, replace `twain.txt` with the `newfilename.txt`, then go to town
- Make the bot send more or fewer tweets, or change which lines, by editing the numbers in `for line in tweettext[0:5]`. 
   - `[0:5]` means from the first thing up to (but not including) the fifth thing
 
 
## Advanced bot: poembot.py

This script treats the poem *This Is Just To Say* (William Carlos Williams) as a mad-lib, filling in 3 blanks from 3 data sources: JSON files from @dariusk's [collection of corpora](https://github.com/dariusk/corpora). 

*Change it up!*
- Choose different [word lists](https://github.com/dariusk/corpora). Make sure to change the URLs in lines ``16-19`` and the list name in lines ``22-25``.
- Choose a different piece of text to make into a mad lib. 

## Commit your changes with Git 

You've made changes to these scripts since you first forked them. Now you'll practice *committing* those changes so you have a record of your versions. 

1. In the Terminal window of VS Code, type `git status` and hit the return (enter) key to see the files you've changed.
1. Then type `git add listbot.py` (or another filename) and hit return
1. (Optional) Type `git status` and hit return again to check what that did
1. Type `git commit -m "Changed what the bot tweets"` (or another way to describe your change) and hit return

[View an annotated screenshot of how to use Git in VS Code](http://robincamille.com/ncsu/vscode_screenshot_git.png)

### Push your changes with Git 

At some point, you'll want the changes you've committed on your machine to appear on your GitHub repository. 

1. In the Terminal window again, type `git push origin master` and hit the return key. You should see a message of success.

No message of success? Ask a workshop facilitator what's going on. 

---

Questions about these instructions? Contact Robin at rcdavis6@ncsu.edu.

---

This tutorial and its updated materials were originally put together by Robin Davis (@robincamille) and Mark Eaton (github.com/MarkEEaton) for a pre-conference workshop at [Code4Lib 2018](http://2018.code4lib.org/).

See also: Davis, Robin, and Mark Eaton. [Make a Twitter Bot in Python: Iterative Code Examples](http://jitp.commons.gc.cuny.edu/make-a-twitter-bot-in-python-iterative-code-examples/). *Journal of Interactive Technology and Pedagogy* (Blueprints section).  April 2016. (Verbose write-up featuring [code from a previous version](https://github.com/robincamille/bot-tutorial) of this workshop.)
