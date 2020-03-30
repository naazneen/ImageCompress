
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import *
from PIL import Image
import time
import os
  
def home(request): 
    
    if request.method == 'GET':
        form = ImageForm() 
        context = {
        'form' : form, 
        
        }
        return render(request, 'index.html', context)
  
    if request.method == 'POST': 
        form = ImageForm(request.POST, request.FILES) 
        if form.is_valid(): 

            # Save Original Image and get ID
            add = form.save() 
            i_id = add.id

            quality = int(request.POST.get('quality'))
            

            # From Id get original Image path for further conversion
            og_image = Images.objects.get(id=add.id)
            image_url = og_image.original_img  
            
            # Opening image and applying convesion operation   
            img = Image.open(image_url)
            new_name = int(time.time())
            img.save('media/converted/{}.jpeg'.format(new_name), quality=quality)

            # Calculating inage sizes
            original_size = os.stat('media/'+str(image_url)).st_size
            converted_size = os.stat('media/converted/{}.jpeg'.format(new_name)).st_size

            # Updating all data
            Images.objects.filter(id=i_id).update(converted_img='converted/{}.jpeg'.format(new_name), converted_size = converted_size, original_size = original_size)
            images = Images.objects.all().order_by('id').reverse()
            
            
            context = {
                    'form' : form, 
                    'images': images[0],
                    'withquality': quality,
                    }
            #return redirect(request.META['HTTP_REFERER'],context)
            return render(request, 'index.html', context)
            

    form = ImageForm() 
    context = {
        'form' : form, 
        
        }
    return render(request, 'index.html', context) 

