from django.db import models


class App(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photos')
    photo_mod = models.ImageField(upload_to='photos_mod', blank=True, null=None)
    created_at = models.DateTimeField(auto_now=True)
    width = models.IntegerField(null=True)
    height = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.title
