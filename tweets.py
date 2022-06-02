from snscrape.modules import twitter 
import pandas as pd
import time

query = "(from:BillGates) until:2022-01-01 since:2021-01-01"
limit = 1000
tweets = []

s = time.time()

for tweet in twitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date.date(), tweet.content, tweet.user.username, tweet.url])
        # print(vars(tweet))
        # break

print(time.time() - s)

df = pd.DataFrame(tweets, columns=["Date", "Content", "Username", "URL"])
df.to_excel("tweets.xlsx")