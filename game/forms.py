from django import forms
from django.forms import widgets
from .models import *


class game_form(forms.ModelForm):
    class Meta:
        model = game
        fields = [
            'fa_name',
            'en_name',
            'brand',
            'scenario',
            'roles',
            'descriptions',
            'unique_description',
            'teaser',
            'poster',
            'price',
            'url',

        ]
        widgets = {
            'fa_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام فارسی بازی ', 'type':'text'  }),
            'en_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام انگلیسی بازی ', 'type':'text'  }),
            'brand': forms.Select(attrs={ 'class':'form-control', 'placeholder': ' نام مجموعه ', 'type':'text'  }),
            'scenario': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' سناریو بازی ', 'type':'text'  }),
            'roles': forms.TextInput(attrs={'class':'form-control', 'placeholder': ' قوانین بازی ', 'type':'text'  }),
            'descriptions': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' توضیحات بازی ', 'type':'text'  }),
            'unique_description': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' توضیحات منحصر به فرد ', 'type':'text'  }),
            'teaser': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' تیزر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/uploadvideo.jpg', 'data-max-file-size':'100M' }),
            'poster': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
            'price': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' قیمت به تومان بدون 3 صفر ', 'type':'number'  }),
            'url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام انگلیسی بازی بدون فاصله ', 'type':'text'  }),
        }

class game_det_form(forms.ModelForm):
    class Meta:
        model = game_details
        fields = [
            'age',
            'hardship',
            'player_from',
            'player_to',
            'time',
            'short_address',
            'full_address',

        ]
        widgets = {
            'age': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' سن مجاز بازی ', 'type':'text'  }),
            'hardship': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' سختی از 10 ', 'type':'text'  }),
            'player_from': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' از نفر ', 'type':'text'  }),
            'player_to': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' تا نفر ', 'type':'text'  }),
            'time': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' زمان بازی به دقیقه ', 'type':'text'  }),
            'short_address': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' ادرس کوتاه ', 'type':'text'  }),
            'full_address': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' ادرس کامل ', 'type':'text'  }),
            
        }

class game_time_form(forms.ModelForm):
    class Meta:
        model = game_time
        fields = [
            'time_from',
            'time_to',
        ]
        widgets = {
            'time_from': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' سانس از ', 'type':'text'  }),
            'time_to': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' سانس تا ', 'type':'text'  }),
        }



class genre_form(forms.ModelForm):
    class Meta:
        model = genre
        fields = [
            'fa_name',
            'en_name',

        ]
        widgets = {
            'fa_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام فارسی  ', 'type':'text'  }),
            'en_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام انگلیسی  ', 'type':'text'  }),
        }

