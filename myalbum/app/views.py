from django.shortcuts import render
from .forms import AddForm



def resize(request):
    if request.method == 'POST':
        form = AddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            img_obj = form.instance
            return render(request, 'app/resize.html', {'form': form, 'img_obj': img_obj})
    else:
        form = AddForm()
    return render(request, 'app/resize.html', {'form': form})
