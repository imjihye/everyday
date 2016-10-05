from django.db import models

# Create your models here.

class Sense(models.Model):
	title = models.CharField(max_length=20)
	subtitle = models.CharField(max_length=20)
	contents = models.TextField(null=True, blank=True)
	create_date = models.DateTimeField(auto_now=True)
	update_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title