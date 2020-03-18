import urllib
from bs4 import BeautifulSoup
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

my_url = 'https://www.foxnews.com'

dt = urllib.request.urlopen(my_url, timeout=0.5)
soup = BeautifulSoup(dt, "lxml")

a = soup.find_all('h2', 'title')
news = []
for ref in a:
  news.append(ref.a.string)

cnt = Counter()
for item in news:
  for word in item.split(" "):
    if word.istitle():
      cnt[word] += 1
com = cnt.most_common(10)
freqs = []
people = []
for x,y in com:
  people.append(x)
  freqs.append(y)

y_pos = np.arange(len(people))
fig, ax = plt.subplots()
ax.barh(y_pos, freqs, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()
ax.set_xlabel('Mentions')
ax.set_title(my_url)
plt.show()