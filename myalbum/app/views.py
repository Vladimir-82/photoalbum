from django.shortcuts import render
from django.core.files.base import ContentFile
from django.http import HttpResponse

from .forms import AddForm
from .models import App

from PIL import Image
from io import BytesIO




def resize(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        photo = request.FILES['photo']


        if form.is_valid():
            sizes = []
            photos = App.objects.all()
            for ph in photos:
                sizes.append(ph.photo_mod.size)


            image = Image.open(photo)
            width, height = image.size
            if request.POST['width'] and request.POST['height']:
                width_new, height_new = request.POST['width'], request.POST['height']

            else:
                width_new = request.POST['width']
                height_new = (int(width) / int(request.POST['width'])) * int(height)


            form.save()
            photo_obj = App.objects.latest('created_at')



            im = image.resize((int(width_new), int(height_new)), Image.ANTIALIAS)
            buffer = BytesIO()
            im.save(fp=buffer, format='webp')
            name = f'{hash(photo_obj.photo)}_{width_new}x{height_new}.webp'

            photo_obj.photo_mod.save(name=name, content=ContentFile(buffer.getvalue()), save=False)
            photo_obj.save()
            if photo_obj.photo_mod.size in sizes:
                return HttpResponse('You have already converted this file!!!')
            return render(request, 'app/resize.html', {'photo_obj': photo_obj})

    else:
        form = AddForm()
    return render(request, 'app/resize.html', {'form': form})
