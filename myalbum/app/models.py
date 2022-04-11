from django.db import models
from PIL import Image




class App(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos')
    photo_mod = models.ImageField(upload_to='photos_mod', blank=True, null=None)
    created_at = models.DateTimeField(auto_now=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True, blank=True)





    def save(self, *args, **kwargs):
        im = Image.open(self.photo)
        print(*args, '!!!')
        print(**kwargs)
        width, height = im.size
        print(width, height, '@@')


        super().save(*args, **kwargs)


    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.title
