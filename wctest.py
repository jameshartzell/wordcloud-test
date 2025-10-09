import pandas as pd
import re,json,requests
from wordcloud import STOPWORDS
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

def clean_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    clean_text = soup.get_text()
    clean_text = re.sub(r'[^\x00-\x7F]+', '', clean_text)  # Remove non-ASCII characters
    return clean_text.strip()

un,server='',''
handle = '@bimmer@mastodon.social'
handle = handle.split('@')
if len(handle) == 3 and handle[0] == '': un,server = handle[1],handle[2]
if len(handle) == 2: un,server = handle[0],handle[1]

URL = f'https://{server}/api/v1/accounts/lookup?acct=@{un}'
idr = json.loads(requests.get(URL).text)
if 'id' in idr.keys(): uid=idr['id']
URL= f'https://{server}/api/v1/accounts/{uid}/statuses'
params = {'limit': 500}
words = []
toots=json.loads(requests.get(URL,params=params).text)
if len(toots)>0:
    for t in toots:
        if 'content' in t.keys():
            content = clean_text(t['content'])
            for w in content.split():
                words.append(w)

text = ' '.join(words)
text = re.sub(r'[^A-Za-z\s]', '', text)
text = text.lower()
stopwords = set(STOPWORDS)
text = ' '.join(word for word in text.split() if word not in stopwords)

wordcloud = WordCloud(width=1920, height=1080, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.title(f'@{un}@{server}')
plt.show()
