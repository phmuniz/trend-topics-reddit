# trend-topics-reddit
O objetivo deste repositório é implementar um código em Python para fazer um trend-topics das palavras mais comentadas de um subreddit. Para isso foi utilizada uma api do Reddit disponibilizada nas referências, manipulada com o pacote do Python Praw. 

## Como funciona?
Você pode rodar o código no terminal com:
```bash
python3 main.py
```
Após isso, será solicitada da entrada o nome de um subreddit a ser analisado, um intervalo de datas, e um número N de palavras. A saída é um arquivo JSON com as N palavras mais comentadas daquele subreddit, naquele intervalo de datas.

## Referências
- <a href="https://www.reddit.com/dev/api/">Reddit API</a>
- <a href="https://www.geeksforgeeks.org/python/how-to-get-client_id-and-client_secret-for-python-reddit-api-registration/">Como fazer as credenciais para usar a API</a>
- <a href="https://praw.readthedocs.io/en/stable/index.html">Documentação do Praw</a>

