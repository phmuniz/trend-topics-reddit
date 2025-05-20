from reddit_api import trend_topics_subreddit
import json

subreddit = input('Informe um subreddit: ')
date_start = input('Qual a data de início? ')
date_end = input('Qual a data final? ')
size = int(input('Qual o número de palavras no trend topics? '))

file_json = open('trend_topics.json', 'w')

trend_topics = trend_topics_subreddit(subreddit, date_start, date_end, size)

json.dump(trend_topics, file_json, indent=4)

file_json.close()