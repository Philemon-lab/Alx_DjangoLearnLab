from django import forms
from .models import Book



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
class BookSearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book Title")
    author = forms.CharField(max_length=100, label="Author Name")
    published_date = forms.DateField(label="Published Date", widget=forms.SelectDateWidget)
    