from django import forms
from .models import *


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Advertisment
        #fields = '__all__'
        fields = ['title','slug','price','descript','place','cat','photo']
        widgets = {
            'title': forms.TextInput(attrs={'class':'text-box'}),
            'descript': forms.Textarea(attrs={'cols':60, 'rows':10})
        }


class AddItemForm___(forms.Form):
    title = forms.CharField(max_length=50)
    slug = forms.SlugField(max_length=50)
    price = forms.IntegerField()
    descript = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':20}))
    place = forms.CharField(max_length=255)
    cat = forms.ModelChoiceField(queryset=Advertisment.objects.all())