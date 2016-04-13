from django.db import models

# Create your models here.


class Diary(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, null=True)
    contents = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
