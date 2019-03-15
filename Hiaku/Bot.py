import tweepy
class Bot(object):

	def __init__(self, API_key, API_secret_key, access_token, access_token_secret):
		self.API_key = API_key
		self.API_secret_key = API_secret_key
		self.access_token = access_token
		self.access_token_secret = access_token_secret

	
	def connect(self,API_key, API_secret_key, access_token, access_token_secret):
		"""Establish a connection to the users Twitter account"""
		authentication = tweepy.OAuthHandler(API_key, API_secret_key)
		authentication.set_access_token(access_token, access_token_secret)

		api = tweepy.API(authentication)

		return api

	def post_tweet(self,api,message):
		api.update_status(message)