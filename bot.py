#imports
import datetime
import json
from requests import get
import tweepy
from time import sleep,time
import random
#api data
api_key = "5KUY8J2QnLFZO4ESW8Ztb2nIX"
api_secret = "2whG3WYr1c011s0xH1jNIiggYmITj9yoh92WGfWeJUFgEclkwo"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAH%2BljgEAAAAAIgm2t4TjDW4YDaK%2Feg749zeY6p0%3DdRuXg70w66MLSLbRBi8BC0xKiBcqCd8f5SGjcu6AJFxgpYN8r7"
access_token = "1595515783106420736-wvVNjzWFeExBi1Xskmxdsly1yPJRBd"
access_secret = "jQ6rVxMmowpm3KOGxrdPpzQbv3kl4vrHERBbci6XrCus8"

#creating access
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_secret)
api = tweepy.API(auth)
#creating message
def price(list, i, key, time1):
    a = random.randint(0, 10)
    message = f"Prices at {time1} \n \n"
    for element in list:
        URL = key + list[i]
        data = get(URL)
        data = data.json()
        message += f"{data['symbol']} price is {data['price']} \n \n"
        i += 1
    message += f'Good luck Whales🐳\n'
    message += f"#crypto #btc #eth #bnb #xrp #ada #staySAFU #{a}"
    client.create_tweet(text=message) #send message
    sleep(300) #wait 5 mins

#loop
while True:
    price(["BTCUSDT","ETHUSDT","BNBUSDT","XRPUSDT","ADAUSDT"],0,"https://api.binance.com/api/v3/ticker/price?symbol=",datetime.datetime.utcnow())
