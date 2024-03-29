from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name=forms.CharField(label='First Name',max_length=100)
#     last_name=forms.CharField(label='Last Name',max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here',
#                              widget=forms.Textarea(attrs={'class':'myform',
#                              'rows':'2','cols':'10'}))
    
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

        labels = {
            'first_name':"Your first name plz",
            'last_name':'Last Name plz',
            'stars':'Rating'

        }

        error_messages ={
            'stars':{
                'min_value':'this value is very low',
                'max_value': 'this value is too much'

            }
        }

        

    


    