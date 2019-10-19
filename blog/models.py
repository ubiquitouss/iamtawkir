from django.db import models

# Create your models here.


class blog(models.Model):
    title = models.CharField(max_length=255, default='your title')
    pub_date = models.DateTimeField()
    body = models.TextField(default='SAY SOMETHIG')
    image = models.ImageField(upload_to="images/")

    # this function is for the title details in admin page
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_st(self):
        return self.pub_date.strftime('%b %e %Y')
