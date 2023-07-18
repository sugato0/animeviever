from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Video
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
def video_list(request,series_id):
    videos = Video.objects.get(id = 1)
    
    
    return render(request, 'viever/video_list.html', {'video': videos,"now":series_id})
    