from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Member,Entry
from .models import Pupil



class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User  # Assuming your User model is imported
        fields = ['username', 'email', 'password1', 'password2']



#creating CRUD
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone', 'joined_date','photo']



class TopicForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname','lastname']
        labels = {'firstname': '',}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Pupil
        fields = ['name','score_1', 'score_2', 'score_3', 'score_4',]