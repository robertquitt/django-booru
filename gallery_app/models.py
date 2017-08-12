import os

from django.db import models

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image, ImageOps

# Create your models here.
def image_upload_path(instance, filename):
    instance.filename = str(filename)
    head, ext = os.path.splitext(filename)
    count = Image.objects.all().count()
    return 'images/{0:03d}/{1:06d}-{2}{3}'.format(count//100, count, head, ext)


class Text(models.Model):
    text = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True, editable=False)


class Image(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to=image_upload_path, editable=False)
    # thumb = models.ImageField(upload_to='images/thumbnails/', editable=False)
    filename = models.CharField(max_length=256, editable=False)
    uploaded = models.DateTimeField(auto_now_add=True, editable=False)
    tags = models.ManyToManyField('Tag', related_name='images')

    # def save(self, content, save=True):
    #     super(Image, )
    #     img = Image.open(self.image.name)
    #     thumb = img.thumbnail((150, 150), Image.NEAREST)
    #     super(Image, self).save()


    def __str__(self):
        return "Image: {0}: {1}".format(self.title, self.filename)


class Tag(models.Model):
    label = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self):
        return "Tag: {0}".format(self.label)
