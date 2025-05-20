import praw
from datetime import date
import re
import os
from dotenv import load_dotenv

def trend_topics_subreddit(subreddit_name: str, date_start_string: str, date_end_string: str, size: int):

    day_start, month_start, year_start = date_start_string.split('/')
    date_start = date(int(year_start), int(month_start), int(day_start))

    day_end, month_end, year_end = date_end_string.split('/')
    date_end = date(int(year_end), int(month_end), int(day_end))

    arq = open("stopwords.txt",'r')
    stop_words = arq.readlines()
    for k in range(len(stop_words)):
        stop_words[k] = stop_words[k].replace("\n","")
    arq.close()

    load_dotenv()

    reddit = praw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        user_agent="phmunizc",
    )

    subreddit = reddit.subreddit(subreddit_name)

    posts = subreddit.top(limit = None)

    trend_topics = {}

    for post in posts:
        time_stamp = post.created_utc
        created_at = date.fromtimestamp(time_stamp)
        
        if date_start <= created_at <= date_end:

            title = clean_text(post.title)
            selftext = clean_text(post.selftext)

            text = title + ' ' + selftext

            words = text.split(" ")

            for word in words:
                
                if word in stop_words or word == '':
                    continue
                if word in trend_topics:
                    trend_topics[word] += 1
                else:
                    trend_topics[word] = 1

    trend_topics = sorted(trend_topics.items(), key=lambda item: item[1], reverse=True)
    trend_topics = dict(trend_topics[:size])

    return trend_topics

def clean_text(text):
    # Substituir quebras de linha e tabulações por espaço
    text = text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

    # Remover pontuação (qualquer caractere que não seja letra, número ou espaço)
    text = re.sub(r'[^\w\s]', '', text)

    # Substituir múltiplos espaços por um único espaço
    text = re.sub(r'\s+', ' ', text)

    # Remover espaços no início e fim
    text = text.strip()

    text = text.lower()

    return text