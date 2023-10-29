from django import forms
from app.models import *
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=['title','image']
class ImageSearchForm(forms.Form):
    search_query=forms.CharField(label='search for images',required=False)