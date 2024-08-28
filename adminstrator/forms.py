from django import forms
from django.forms import widgets
from .models import *
from brand.models import brand

class admin_info_form(forms.ModelForm):
    class Meta:
        model = admin_info
        fields = [
            'first_name',
            'last_name',
            'gender',

        ]
        widgets = {
            'first_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام  ', 'type':'text'  }),
            'last_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام خانوادگی ', 'type':'text'  }),
            'gender': forms.Select(attrs={ 'class':'form-control', 'placeholder': ' جنسیت ', 'type':'text'  }),
        }

class admin_login_form(forms.ModelForm):
    class Meta:
        model = admin_login
        fields = [
            'password',
            'phonenumber',
            'admin_type',
            'brand',

        ]
        widgets = {
            'password': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' رمز عبور ', 'type':'text'  }),
            'phonenumber': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' تلفن همراه ', 'type':'text'  }),
            'admin_type': forms.Select(attrs={ 'class':'form-control', 'placeholder': ' نوع کاربری ', 'type':'text'  }),
            'brand': forms.Select(attrs={ 'class':'form-control', 'placeholder': ' نام مجموعه ', 'type':'text'  }),
        }