from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from .models import Anime,Season,Series,User
from .forms import RegistrationForm
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.hashers import make_password



def register(request):
    if request.method == 'POST':
        # Обработка отправленной формы регистрации
        # Получите данные из формы и выполните необходимую обработку
        
        form = RegistrationForm(request.POST)

        if form.is_valid():
            
            # process form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            

            user = User.objects.create_user( username=username, email=email, password=password,is_active= True)
            

            #finally save the object in db
            user.save()
        # Дополнительная логика регистрации

            myuser = authenticate(request, username=username, password=password)
            
            login(request, myuser)

            
        else:
            print(form.error_messages)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            
            login(request, user)
            
        
        return redirect(request.META.get('HTTP_REFERER'))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def main_video_list(request):
    
    anime = Anime.objects.all()
    anime_new = Anime.objects.filter(date_time__gte= datetime.now() - timedelta(days=30))
    
    
    
    return render(request, 'viever/main_video_list.html',context =  {"anime_list":anime,"anime_new":anime_new,})
    
        

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
    
    
   
    return render(request, 'viever/anime_profile.html',context =  {"anime":anime,
                                                         "seasons":seasons,
                                                         'series_list': series_list,
                                                         "genres":anime.genre.replace("'"," ").replace("["," ").replace("]"," "),
                                                         
                                                         })
def profile(request):
    
    
    
    return render(request, 'person_pages/index.html',context =  {})


def search_anime(request):
    query = request.GET.get('query')
    
    anime_list = Anime.objects.filter(name=query)
    
    return render(request, 'viever/search.html',context =  {'anime_list': anime_list,})





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
    

    
    
    
    
    return render(request, 'viever/video_list.html', context = {'video': series,
                                                      "id":id,
                                                      "name":name,
                                                      "now_series":series_id,
                                                      "now_season":season_id,
                                                      "max_series":max_series,
                                                      "max_seasons":max_seasons,
                                                      "last_series":last_series,
                                                        })

    