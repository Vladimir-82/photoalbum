from django.db import models


class App(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_out = models.ImageField(upload_to='photos_out/%Y/%m/%d/', blank=True, null=None)


    def __str__(self):
        return self.title
