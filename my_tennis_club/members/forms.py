#import form class from django
from django import forms

# import Member from models.py
from .models import Member

#create a ModelForm
class MemberForm(forms.ModelForm):
    #specify the name of model to use
    class Meta:
        model=Member
        fields="__all__"