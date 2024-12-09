from django.shortcuts import render
import requests
# Create your views here.
API_KEY = 'c8cb3b0e7dbe498981874084d6dec738'


def home(request):

    
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2024-11-09&sortBy=publishedAt&apiKey=c8cb3b0e7dbe498981874084d6dec738'
    response = requests.get(url)
    data = response.json()  # to get all data
    # print(data)

    # in data we have articles and get data of it
    articles = data['articles']

    # To get All data
    # context ={
    #     'data': data
    # }

    # To get article data from API

    context ={
        'articles' : articles
    }

    return render(request,'AppNewsApi/home.html',context)

    