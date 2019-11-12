from django.shortcuts import render
from django.http import HttpResponse
from .models import Search
from django.db.models import Q
from . import twitter_search
# from django.views.generic import CreateView
# 19:56

# Create your views here.

def home(request):
    return render(request, 'pulse_search/home.html')

def about(request):
    return render(request, 'pulse_search/about_pulse.html')

def team(request):
    return render(request, 'pulse_search/pulse_team.html')

def display_results(request):
    #to pull from the database
    # search_term = Search.objects.all(username = user.username).first()???
    #retrieve latest search term from user account
    #run through relavent programs to create a dict of dicts, i.e.:
    # twitter_dict = twitter_search.my_function()
    # context ={
    #     'tweets_dict' : tweets_dict,
    #     'video_dict' : video_dict,
    #     'reddit_dict' : reddit_dict
    # }
    #finally pass into the render request

    context = {'tweets_dict' : twitter_search.tweets_dict}
    #to pull from the database
    # context = {'tweets_dict' : Search.objects.all()}
    return render(request, 'pulse_search/display_results.html', context)
