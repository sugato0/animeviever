from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Anime,Season,Series
from .forms import RegistrationForm
from datetime import datetime, timedelta

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = RegistrationForm()
    return render(request, 'authfiles/registrate.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('video_list')  # Перенаправление на домашнюю страницу
        

    return render(request, 'authfiles/login.html')

# def video_list(request,series_id):
#     videos = Video.objects.get(id = 1)
    
    
#     return render(request, 'viever/video_list.html', {'video': videos,"now":series_id})
def main_video_list(request):
    anime = Anime.objects.all()
    anime_new = Anime.objects.filter(date_time__gte= datetime.now() - timedelta(days=30))
    
    return render(request, 'viever/main_video_list.html', {"anime_list":anime,"anime_new":anime_new})

def anime_detail(request,name):
    anime = Anime.objects.filter(name = name).first()
    
    seasons = Season.objects.filter(anime = anime)
    series_list = {}
    count = 1
    for i in seasons:
        series = Series.objects.filter(season = i)
        listik = []
        for j in series:
            listik.append(j)
        series_list[count] = reversed(listik)
        count+=1
    
    
   
    return render(request, 'viever/anime_profile.html', {"anime":anime,
                                                         "seasons":seasons,
                                                         'series_list': series_list,
                                                         "genres":anime.genre.replace("'"," ").replace("["," ").replace("]"," ")
                                                         })
    

def search_anime(request):
    query = request.GET.get('query')
    
    anime_list = Anime.objects.filter(name=query)
    
    return render(request, 'viever/search.html', {'anime_list': anime_list})





def video_list(request,name,season_id,series_id):
    anime = Anime.objects.filter(name = name).first()
    seasons = Season.objects.filter(anime = anime)
    max_seasons = len(seasons)
    max_series =1
    last_series =1

    seasons = seasons.filter(season_id = season_id).first()
    series = Series.objects.filter(season = seasons)
    if max_series!= len(series):
        last_series = max_series
        max_series = len(series)

    series = series.filter(series_id = series_id).first()
    

    
    
    
    
    return render(request, 'viever/video_list.html', {'video': series,
                                                      "id":id,
                                                      "name":name,
                                                      "now_series":series_id,
                                                      "now_season":season_id,
                                                      "max_series":max_series,
                                                      "max_seasons":max_seasons,
                                                      "last_series":last_series})

    