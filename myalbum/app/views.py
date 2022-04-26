from PIL import Image
from io import BytesIO

import uuid

from django.shortcuts import render
from django.core.files.base import ContentFile
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response

from .forms import AddForm
from .models import App
from .serializers import AppSerializer


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
            hash = uuid.uuid3(uuid.NAMESPACE_DNS, photo_obj.title)
            name = f'{hash}_{width_new}x{height_new}.webp'
            photo_obj.photo_mod.save(name=name, content=ContentFile(buffer.getvalue()), save=False)
            photo_obj.save()
            if photo_obj.photo_mod.size in sizes:
                return HttpResponse('You have already converted this file!!!')
            return render(request, 'app/resize.html', {'photo_obj': photo_obj})

    else:
        form = AddForm()
    return render(request, 'app/resize.html', {'form': form})


class ApiResize(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer

    def post(self, request, *args, **kwargs):
        photo = request.data['photo']

        sizes = []
        photos = App.objects.all()
        for ph in photos:
            sizes.append(ph.photo_mod.size)
        serializer = AppSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        image = Image.open(photo)
        width, height = image.size
        if request.POST['width'] and request.POST['height']:
            width_new, height_new = request.POST['width'], request.POST['height']

        else:
            width_new = request.POST['width']
            height_new = (int(width) / int(request.POST['width'])) * int(height)


        photo_obj = App.objects.latest('created_at')

        im = image.resize((int(width_new), int(height_new)), Image.ANTIALIAS)
        buffer = BytesIO()
        im.save(fp=buffer, format='webp')
        hash = uuid.uuid3(uuid.NAMESPACE_DNS, photo_obj.title)
        name = f'{hash}_{width_new}x{height_new}.webp'
        photo_obj.photo_mod.save(name=name, content=ContentFile(buffer.getvalue()), save=False)
        photo_obj.save()

        if photo_obj.photo_mod.size in sizes:
            return HttpResponse('You have already converted this file!!!')

        return Response(photo_obj.photo_mod.url)
