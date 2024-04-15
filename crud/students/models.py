from django.db import models
from django.urls import reverse

# Create your models here.


class Students(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=25)
    sage=models.IntegerField()
    splace=models.CharField(max_length=25)
    smajor=models.CharField(max_length=10)

    def __str__(self) :
        return self.sname
    
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})