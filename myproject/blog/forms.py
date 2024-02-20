from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        # fields = ['first_name', 'second_name', 'email', 'bio', 'birthdate']
        exclude = ['full_name']
        labels = {'first_name':'Имя', 'second_name':'Фамилия', 'email':'Почта', 'bio':'Биография', 'birthdate':'День рождения'}

class PostForm(forms.Form):

    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    pub_date = forms.DateField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    category = forms.CharField()
    views_count = forms.IntegerField(initial=0)
    ispublic = forms.BooleanField(required=False)

class CommentForm(forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    content = forms.CharField(widget=forms.Textarea)
