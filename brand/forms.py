from django import forms
from django.forms import widgets
from .models import brand, brand_slide


class brand_form(forms.ModelForm):
    class Meta:
        model = brand
        fields = [
            'fa_name',
            'en_name',
            'descriptions',
            'big_logo',
            'sm_logo',
            'url',

        ]
        widgets = {
            'fa_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام فارسی مجموعه ', 'type':'text'  }),
            'en_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام انگلیسی مجموعه ', 'type':'text'  }),
            'descriptions': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' توضیحات مجموعه ', 'type':'text'  }),
            'big_logo': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M', 'accept':'.webp, image/*'}),
            'sm_logo': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' لوگو کوچک ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M', 'accept':'.webp, image/*'}),
            'url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' URL ', 'type':'text'  }),
        }


class sliders_form(forms.ModelForm):
    class Meta:
        model = brand_slide
        fields = [
            'slide',
        ]
        widgets = {
            'slide': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
        }