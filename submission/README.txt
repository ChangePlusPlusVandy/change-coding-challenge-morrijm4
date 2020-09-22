
##Project Description

This project is a game that prompts the user with a tweet from either Kanye West or Elon Musk. Then, the user will then guess who tweeted it and see if they got it right. Once the user is done playing the game then the program will let them know how accurate their guesses were.

##Project Specifications

This program uses Python to request data from the Twitter API.

##Prerequisites 

In order for my code to run successfully you need to make sure you have the requests module on your computer. Provided below are steps on how you can download it on any device

##How to install the request module

There are multiple ways to do this but I have provided the one method that has worked for me.

#macOS or Linux

In order to install the remote module you first need pip. There are multiple 

1. Install homebrew

Run the following command in macOS terminal. 

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"`

2. Install the brew-pip package

Run this command in your terminal.

`brew install brew-pip`

3. Add Homebrew's pip path to your PYTHONPATH environment variable (you probably should add this to some sort of shell initialization file like ~/.bashrc or ~/.zshrc)

Run this command in the terminal.

`export PYTHONPATH=$(brew --prefix)/lib/python2.7/site-packages`

3. Now install the requests module using pip

Run this command in your terminal.

`python -m pip install requests`