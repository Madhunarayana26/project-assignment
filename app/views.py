from django.shortcuts import render,redirect,HttpResponse
from app.models import *
from app.forms import *
# Create your views here.
def upload_image(request):
    if request.method=='POST' and request.FILES:
        form=ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_search')
    else:
        form=ImageUploadForm()
    return render(request,'upload_image.html',{'form':form})

def image_search(request):
        if request.method == 'POST':
            form = ImageSearchForm(request.POST)
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                images = Image.objects.filter(title__icontains=search_query)
        else:
            images = Image.objects.all()
            form = ImageSearchForm()

        return render(request, 'image_search.html', {'images': images, 'form': form})