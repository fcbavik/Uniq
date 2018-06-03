from django import forms
# from django.contrib.auth.models import User
from students.models import User

from .models import Subject, File, Question


# class AlbumForm(forms.ModelForm):
#
#     class Meta:
#         model = Album
#         fields = ['university', 'name', 'genre', 'logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['name', 'file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']
