from django.db import models

# Create your models here.


class Job(models.Model):

    def __str__(self):
        return self.job_summery

    job_image = models.ImageField(upload_to="images/")
    job_summery = models.CharField(max_length=100)
