from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField('ImageFile', related_name='images')

    def __str__(self):
        return self.title

class ImageFile(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.image)
