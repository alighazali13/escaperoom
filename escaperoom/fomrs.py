from django import forms
from django.forms import widgets
from .models import *

class banner_header_form(forms.ModelForm):
    class Meta:
        model = banner_header
        fields = [
            'name',
            'url',
            'slide',
        ]
        widgets = {
            'name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام اسلاید ', 'type':'text'  }),
            'url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' ادرسی که کاربر به آن هدایت خواهد شد ', 'type':'text'  }),
            'slide': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
        }

class sliders_form(forms.ModelForm):
    class Meta:
        model = slides
        fields = [
            'name',
            'url',
            'slide',
        ]
        widgets = {
            'name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام اسلاید ', 'type':'text'  }),
            'url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' ادرسی که کاربر به آن هدایت خواهد شد ', 'type':'text'  }),
            'slide': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
        }


class advbanner_form(forms.ModelForm):
    class Meta:
        model = advertising_banner
        fields = [
            'adv_banner_name',
            'adv_banner_url',
            'adv_banner_slide',
        ]
        widgets = {
            'adv_banner_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام اسلاید ', 'type':'text'  }),
            'adv_banner_url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' ادرس بنر ', 'type':'text'  }),
            'adv_banner_slide': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
        }
    

class advslide_form(forms.ModelForm):
    class Meta:
        model = advertising_slide
        fields = [
            'adv_slide_name',
            'adv_slide_url',
            'adv_slide_slide',
        ]
        widgets = {
            'adv_slide_name': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' نام اسلاید ', 'type':'text'  }),
            'adv_slide_url': forms.TextInput(attrs={ 'class':'form-control', 'placeholder': ' ادرس بنر ', 'type':'text'  }),
            'adv_slide_slide': forms.FileInput(attrs={ 'class':'form-control dropify', 'placeholder': ' پوستر ', 'type':'file', 'data-default-file':'/statics/dashboard/assets/img/2849110.png', 'data-max-file-size':'2M' }),
        }
