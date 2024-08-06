from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .news_api import get_news

# Create your views here.
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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})
