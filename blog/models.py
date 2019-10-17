from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=255, default='your title')
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=255, default='SAY SOMETHIG')
    image = models.ImageField(upload_to="images/")
