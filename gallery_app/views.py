from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Image, Tag
from .forms import ImageUploadForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def image(request, pk):
    image = Image.objects.get(pk=pk)
    tags = image.tags.all()
    return render(request, 'image.html', {'image': image, 'tags': tags})


def tag(request, pk):
    tag = Tag.objects.get(pk=pk)
    images = tag.images.all()
    return render(request, 'tag.html', {'tag': tag, 'images': images})


def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Image(image=request.FILES['image_file'])
            image.save()
            # Redirect to document after POST
            return HttpResponseRedirect(reverse('image', kwargs={'pk': image.id}))
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})


def list(request):
    images = Image.objects.all()
    tags = Tag.objects.all()
    return render(request, 'list.html', {'images': images, 'tags': tags})

