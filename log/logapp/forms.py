from django import forms
from django.forms import ModelForm, Textarea

from .models import Postmsg,Profilecover
class Postmsgform(forms.ModelForm):
    class Meta:
        model=Postmsg
        fields=['text','image','name']
        labels={
            'text':'Message'
        }
        widgets = {
            'text': Textarea(attrs={'cols': 50, 'rows': 5 ,}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
class Profilecoverform(forms.ModelForm):
    class Meta:
        model=Profilecover
        fields=['profile','coverphoto']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile'].required = False
        self.fields['coverphoto'].required = False
    