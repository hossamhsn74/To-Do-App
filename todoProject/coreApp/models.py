from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=400)
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
