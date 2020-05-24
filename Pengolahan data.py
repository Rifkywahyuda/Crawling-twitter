import re
import json
import pandas as pd
import matplotlib.pyplot as plt

tweets_data_path = 'twittermi.txt'

tweets_data = []
tweets_file = open(tweets_data_path, 'r')
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

print(len(tweets_data))
tweets = pd.DataFrame()

def word_in_text(word,text):
    if text == None:
        return False
    word = word.lower()
    text = text.lower()
    match = re.search(word,text)
    if match:
        return True
    else:
        return False

tweets['text'] = [tweet['text'] for tweet in tweets_data]
tweets['python'] = tweets['text'] .apply(lambda tweet: word_in_text('python', tweet))
tweets['javascript'] = tweets['text'] .apply(lambda tweet: word_in_text('python', tweet))
tweets['ruby'] = tweets['text'] .apply(lambda tweet: word_in_text('python', tweet))

print (tweets['python'].value_counts() [True])
print (tweets['javascript'].value_counts() [True])
print (tweets['ruby'].value_counts() [True])

prg_langs = ['python', 'javascript','ruby']
tweets_by_prg_lang = [tweets['python'].value_counts()[True], tweets['javascript'].value_counts()[True], tweets['ruby'].value_counts()[True]]

x_pos = list(range(len(prg_langs)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang, width, alpha = 1, color = 'g')

#setting axis label dan ketebalan
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: python vs. javascript vs. ruby (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p +0.1 *width for p in x_pos])
ax.set_xticklabels(prg_langs)
plt.grid()

plt.show
