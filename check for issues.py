from ast import Str
from os import remove
import matplotlib.pyplot as plt
import constants
import collections
from constants import RAW_TEXT, SUSPICIOUS_KEYWORDS, STOPWORDS, regex_to_use
from collections import Counter
import requests
from bs4 import BeautifulSoup

def sus_word_count(RAW_TEXT, url_input):
    words=regex_to_use(RAW_TEXT)
    # WORDS is used for saving all words that are not in STOPWORDS and that their length is more than 2
    WORDS=[]
    not_suspicious=[]
    for word in words:
        if word in not_suspicious:
            continue
        else:
            if word in STOPWORDS or len(word)<=2:
                not_suspicious.append(word)
                continue
            else:
                WORDS.append(word)
    word_count=Counter(WORDS).most_common(40)
    WORD_COUNT=[]
    for place in range (len(word_count)):
        if word_count[place][0]  in SUSPICIOUS_KEYWORDS:
            WORD_COUNT.append(word_count[place])
            y = list(word_count[place])
            y.append('(suspicious)')
            word_count[place]= tuple(y)
    if len(WORD_COUNT)>=7:
        with open("log.txt", 'a') as f:
            for x in range(30):
                f.write('=')
            f.write('\n')
            f.write('Document URL: ')
            f.write(url_input)
            f.write('\n')
            for t in word_count:
                f.write(' '.join(str(s) for s in t) + '\n')
            f.write('Document is classified as suspicious.  \n')
    else:
        with open("log.txt", 'a') as f:
            for x in range(30):
                f.write('=')
            f.write('\n')
            f.write('Document URL: ')
            f.write(url_input)
            f.write('\n')
            for t in word_count:
                f.write(' '.join(str(s) for s in t) + '\n')
            f.write('Document does not appear as suspicious.  \n')
    return word_count


def main(save_database):
    paragraph=save_database
    word_count = sus_word_count(paragraph)
    categories = []
    values = []
    paint=[]
    for j in range(len(word_count)):
        categories.append(word_count[j][0])
        values.append(word_count[j][1])
        if len(word_count[j])==3:
            paint.append('red')
        else:
            paint.append('grey')
    plt.figure(figsize=(8, 4))
    plt.bar(categories, values, color=paint)
    plt.title('Top 40 words(suspicious in red)')
    plt.xticks(rotation=80)
    plt.show()

main()
