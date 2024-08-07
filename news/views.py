from django.shortcuts import render
from .news_api import get_news

def home(request):
    country = request.GET.get('country', 'us')
    category = request.GET.get('category', 'general')
    page = int(request.GET.get('page', 1))
    
    news = get_news(country=country, category=category, page=page)
    articles = news.get('articles', [])

    return render(request, 'cards/home.html', {
        'news': articles,
        'country': country,
        'category': category,
        'page': page,
        'has_more': len(articles) == 20 
    })
