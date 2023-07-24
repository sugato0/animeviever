from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Anime

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

GENRES= (
    ('Повседневность', 'Повседневность'),
    ('Романтика', 'Романтика'),
    ('Драмма', 'Драмма'),
    ('Экшн', 'Экшн'),
    ('Ужасы', 'Ужасы'),
)

class AnimeAdminForm(forms.ModelForm):
    genre = forms.MultipleChoiceField(choices=GENRES)

    class Meta:
        model = Anime
        fields = '__all__'
