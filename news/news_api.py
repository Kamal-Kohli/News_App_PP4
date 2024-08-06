import requests

NEWS_API_KEY = '2228671f48644d399e8cc37fb14015f6'

def get_news(country='us', category='general', page=1, page_size=20):
    url = (f'https://newsapi.org/v2/top-headlines?country={country}'
           f'&category={category}&page={page}&pageSize={page_size}&apiKey={NEWS_API_KEY}')
    response = requests.get(url)
    return response.json()
