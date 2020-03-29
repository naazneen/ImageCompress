from django import forms 
from .models import *
from django_range_slider.fields import RangeSliderField
  
class ImageForm(forms.ModelForm): 
  
    class Meta: 
        model = Images 
        fields = ['original_img', 'quality'] 