from django.db import models


class job(models.Model):
    title = models.CharField(max_length=200, default="title")
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200, default="summary")

    def __str__(self):
        return self.title
