import tweepy as tw
import random

consumer_key = 'Q0VGMAXKdyZ6Jcen6FyOWQ9Xf'
consumer_secret = '5ZLUDaGNLTHTh6u8x6RbCucwM1tTytDWI2VMUmB1wxMCPE77wX'
access_token = '2857083446-jfYg8hpCkWF3JRNDjcKo1rgHwKDNQvPMTDcdPW7'
access_token_secret = 'fiTGhnJ3UqIrqjI7Jn3OVR6bnu88LrRivolY9Xo5yfPIg'

# Authorization to consumer key and consumer secret
auth = tw.OAuthHandler(consumer_key, consumer_secret)

# Access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# Calling api
api = tw.API(auth)

# Constant
NUM_OF_TWEETS = 3200
ATTEMPTS = 0
CORRECT = 1


# Function to welcome the user to the game
def welcome_user():
    print("Welcome to Can You Guess It!?")
    print("In this game you will be given a tweet from either Kanye West or Elon Musk")
    print("and your job is to guess who tweeted the tweet.\n")
    print("Please wait just a moment.\n")


# Function to thank user for playing class when the user is done playing
def thank_user(stats):
    attempts = stats[ATTEMPTS]
    correct = stats[CORRECT]

    print("\nThank you for playing!")
    print("\nHere are some statistics to see how you did!")
    print("\tTotal Attempts: " + str(attempts))
    print("\tTotal Correct Attempts: " + str(correct))
    print("\tWin Ratio: " + str(float(correct) / float(attempts)))


# Function used to determine if the user wants to play again
def playAgain():
    while True:
        ready = raw_input("Would you like to play again Y/N?\n").lower().strip()
        if ready[0] == "y":
            break
        elif ready[0] == "n":
            break
        else:
            print("Please enter Y or N")

    return ready


# Function to extract tweets
def get_tweets(username):
    # 200 tweets to be extracted
    tweets = api.user_timeline(screen_name=username, count=NUM_OF_TWEETS)

    # Empty Array
    tmp = []
    tws = []
    final = []

    # create array of tweet information: username,
    # tweet id, date/time, text
    tweets_for_csv = [tweet.text for tweet in tweets]  # CSV file created
    for j in tweets_for_csv:
        # Appending tweets to the empty array tmp
        tmp.append(j)

    # Get rid of the links
    for t in tmp:
        pos = t.find("https://")
        if pos == 0:
            None
        elif pos != -1:
            tws.append(t[:pos])

    # Get rid of @user's
    for t in tws:
        pos = t.rfind("@")
        if pos != -1:
            t_str = t[pos:]
            space = t_str.find(" ") + 1
            final.append(t_str[space:])
        else:
            final.append(t)

    # Return the tweets
    return final


# Global Variables
attempts = 0  # Tracks how many attempts they have made
correct = 0  # Tracks how many attempts were correct


def isCorrect(rNum, stats):
    tmp = stats[ATTEMPTS]
    while stats[ATTEMPTS] == tmp:

        # Input user's guess
        guess = raw_input("Who tweeted it? Kanye or Elon?\n").lower().strip()

        # if kanye is the correct answer
        if rNum == 1:
            if (guess == "kanye") or (guess == "kanyewest") or (guess == "kanye west"):
                print("Congrats! You are correct!")
                stats[CORRECT] += 1
                stats[ATTEMPTS] += 1

            elif (guess == "elon") or (guess == "elonmusk") or guess == ("elon musk"):
                print("I'm sorry, Kanye tweeted this :(")
                stats[ATTEMPTS] += 1

            else:
                print"Whoops! I think you might have spelled that wrong. Try again!"

        # if elon is the correct answer
        else:
            if (guess == "elon") or (guess == "elonmusk") or guess == ("elon musk"):
                print("Congrats! You are correct!")
                stats[CORRECT] += 1
                stats[ATTEMPTS] += 1

            elif (guess == "kanye") or (guess == "kanyewest") or (guess == "kanye west"):
                print("I'm sorry, Elon tweeted this :(")
                stats[ATTEMPTS] += 1

            else:
                print"Whoops! I think you might have spelled that wrong. Try again!"


# ============
# MAIN METHOD
# ============

welcome_user()

# Where Kanye and Elon's tweets are extracted
kanye = get_tweets("kanyewest")
elon = get_tweets("elonmusk")

# Wait for until the user is ready to begin playing
ready = 'n'
while ready[0] != "y":
    ready = raw_input("When you are ready to begin press Y\n").lower().strip()

print("Okay! Lets go..\n")

# Keep track of stats
# [attempts, correct]
stats = [0, 0]

# Heart of the game
while ready[0] == "y":

    # Randomly select 1 or 2
    rNum = random.randint(0, 2)

    length = None
    if (rNum == 1):
        length = len(kanye)
    else:
        length = len(elon)

    # Random number to select tweet
    rTweet = random.randint(0, length)

    # Get tweet for either Kanye or Elon
    tweet = None
    if rNum == 1:
        tweet = kanye[rTweet]
    else:
        tweet = elon[rTweet]

    # Prompt user the tweet
    print("Attempt: " + str(attempts + 1))
    print("==========\n")
    print(tweet + "\n")

    # Hey Change++ I realise this is super ugly I just did not have much time.
    isCorrect(rNum, stats)

    # determine if the user wants to keep going
    ready = playAgain()

thank_user(stats)
