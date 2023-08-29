from django.db import models
from django.contrib.auth.models import User

class Tez(models.Model):
    baslik = models.CharField(max_length=200)
    yazar = models.CharField(max_length=100)
    dosya = models.FileField(upload_to='tezler/')  # 'media/tezler/' altına kaydedilecek
    dosya_converted = models.FileField(upload_to='thesis_converted/', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)




    def __str__(self):
        return self.baslik
