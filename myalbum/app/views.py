from django.shortcuts import render
from .models import App
from .forms import AddForm



def resize(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        print(request.POST['width'])
        # print(request.FILES)
        if form.is_valid():

            if request.POST['width'] and request.POST['height']:
                width, height = request.POST['width'], request.POST['height']
            else:
                pass


            form.save()

            img_obj = form.instance
            return render(request, 'app/resize.html', {'form': form, 'img_obj': img_obj,
                                                       'width':width,'height':height })
    else:
        form = AddForm()
    return render(request, 'app/resize.html', {'form': form})
