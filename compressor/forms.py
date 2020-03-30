from django import forms 
from .models import *
#from django_range_slider.fields import RangeSliderField
  
class ImageForm(forms.ModelForm): 
    quality = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '100','onchange':'updateTextInput(this.value);'}), required=False) 
  
    class Meta: 
        model = Images 
        fields = ['original_img', 'quality'] 
        
        