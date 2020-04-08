from django.db import models

# Create your models here.


class Blog(models.Model):
    def __str__(self):
        return self.title


    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    body = models.CharField(max_length=300)
    image = models.ImageField(upload_to="images/")
