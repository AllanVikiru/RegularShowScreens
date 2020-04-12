#  bot for tweeting
import random  # module for randomising variables
import tweepy as twt  # library for accessing twitter api
import time  # time module
import os  # os module
import credentials as app  # fetch twitter credentials

first_tweet = 'Don\'t mind this tweet. It\'s a test 👀'
first_reply = 'Aye! It works 🤩 '
# after sending out the first tweet, ctrl c + ctrl v the tweet id from the tweet url:
# https://twitter.com/{your_account}/status/{tweet_id}
first_tweet_id = 0

interval: int = 30  # set interval to 30 seconds

# authentication to twitter account
auth = twt.OAuthHandler(app.API_KEY, app.API_SECRET)
auth.set_access_token(app.ACCESS_TOKEN, app.ACCESS_SECRET)
api = twt.API(auth)


# send out first tweet
def first():
    try:
        api.update_status(first_tweet)
        quit("Kaende kaende")  # Sheng version of 'Ayyyyyyy'
    except Exception as e:
        quit(e)
        pass


# reply to first tweet
def reply():
    try:
        api.update_status(first_reply, first_tweet_id)
        quit("Last tweet fr fr")  # I say this A LOT
    except Exception as e:
        quit(e)
        pass


# tweet scraped images
def screen():
    # access and select screenshots folder
    os.chdir('screens')
    frames = os.listdir('.')

    while True:
        try:
            # loop over images
            for frame in frames:
                frame = random.choice(frames)  # select random image
                api.update_with_media(frame)  # tweet image
                print("I'll be back")  # a Terminator reference
                time.sleep(interval)  # wait 30 seconds to tweet next image
        except Exception as e:
            print(e)
            pass


while True:
    print("TWITTERRRRR")  # a Brooklyn Nine-Nine reference
    screen()
