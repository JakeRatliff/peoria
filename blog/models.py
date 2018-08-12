from django.db import models

# Create your models here.

class Blog(models.Model):
	image = models.ImageField(upload_to = 'images/')
	title = models.CharField(max_length = 70)
	pub_date = models.DateTimeField()
	body = models.CharField(max_length = 20000)

	def summary(self):
		return self.body[:100]

	def __str__(self):
		return self.title