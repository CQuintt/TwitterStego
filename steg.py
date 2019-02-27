import tweepy
import time
import datetime
import schedule
import string

current_time = time.time()
timeString = datetime.datetime.fromtimestamp(current_time).strftime('%H:%M:%S')

API_key = "u1NpPWoQ0klxIE1tnEfeeKfLa"
API_secret_key = "XxFJecfOJtnG4WdLgMAvGPNkyEmSavw8tPfIExR8VCURGV4Rbn"
access_token = "1088648194555289600-weVaU8a1hTZ8st6zUfVaQvfiL8L09M"
access_token_secret = "afKljvXSZzyBHwHDsgwCGE6BdBSuq2K2qRuK5Js92vjLy"

API_keys = []
API_secrey_keys = []
access_tokens = []
access_token_secrets = []

auth = tweepy.OAuthHandler(API_key,API_secret_key)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

tweet_timestamps = []

def post_tweet(message):

	api.update_status(message)

def time_post():
	while True:
		schedule.run_pending()

def get_timestamps(tweet):

	#tweet_timestamps.append(tweet.created_at)
	file = open("tweetData.txt","w")
	file.write(str(tweet))

def get_tweets():

	tweet_list = []
	account = api.get_user("StartedBot")
	all_tweets = api.user_timeline(account)

	for tweets in all_tweets:
		if(tweets.text.__contains__("#cqhwsteg")):
			tweet_list.append(tweets.text)
			get_timestamps(tweets)

	return tweet_list

def get_message(tweet_list):

	message = ""
	for i in range(0,len(tweet_list)):

		position1 = tweet_timestamps[i].strftime("%M")[0]
		position2 = tweet_timestamps[i].strftime("%M")[1]

		word_list = tweet_list[i].split()

		message = '' + " " + word_list[int(position1) - 1] + " " + word_list[int(position2) - 1] + message

	print(message[0])


#schedule.every().day.at("07:34:40").do(post_tweet,"testing testing Meet me testing testing testing testing tetsing #cqhwsteg")
#schedule.every().day.at("07:35:40").do(post_tweet,"testing testing at testing the tetsing testing tetsing #cqhwsteg")
#schedule.every().day.at("07:36:40").do(post_tweet,"testing testing park testing tetsing come tetsing #cqhwsteg")
#schedule.every().day.at("07:37:40").do(post_tweet,"testing testing alone tetsing tetsing testing . #cqhwsteg")



#time_post()
#get_timestamp()
get_message(get_tweets())