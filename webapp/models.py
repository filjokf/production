from django.db import models

class production(models.Model):
	api_wellnumber=models.TextField()
	oil=models.TextField()
	gas=models.TextField()
	brine=models.TextField()


	def __str__(self):
		return self.api_wellnumber


