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
            image = Image.open(photo)
            width, height = image.size
            if request.POST['width'] and request.POST['height']:
                width_new, height_new = request.POST['width'], request.POST['height']

            else:
                width_new = request.POST['width']
                height_new = (int(width) / int(request.POST['width'])) * int(height)


            form.save()
            p = App.objects.latest('created_at')

            im = image.resize((int(width_new), int(height_new)), Image.ANTIALIAS)
            buffer = BytesIO()
            im.save(fp=buffer, format='webp')
            name = f'{hash(p.photo)}_{width_new}x{height_new}.webp'

            p.photo_mod.save(name=name, content=ContentFile(buffer.getvalue()), save=False)


            img_obj = form.instance
            return render(request, 'app/resize.html', {'form': form, 'img_obj': img_obj,
                                                       'width': width_new, 'height': height_new,
                                                       })

    else:
        form = AddForm()
    return render(request, 'app/resize.html', {'form': form})
