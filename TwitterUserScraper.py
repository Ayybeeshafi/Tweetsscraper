import pandas as pd
import snscrape.modules.twitter as sntwitter
maxTweets = 7000

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:ImranKhanPTI').get_items()):
    if i>maxTweets:
        break
    tweets_list1.append([tweet.content])
#Storing tweets contents in a dataframe
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Content'])
tweets_df1.to_csv('ImranKhanPTI.csv', sep=' ', index=False)
#print(tweets_list1)
file = open("", "rt", encoding="utf8")
text = file.read()
#Removing non english characters
encoded_string = text.encode("ascii", "ignore")
encoded_string = filter(lambda char: char not in "\n", encoded_string)
f = open("", "a")
f.write(str(encoded_string))
f.close()

