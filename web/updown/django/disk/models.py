from django.db import models

def get_photo_path(instance, filename):  
	productionName = instance.username  
	return './upload/%s/%s' % (productionName,filename)  
#	return name  

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length = 30)
#	headImg = models.FileField(upload_to = './upload/meng/')
	headImg = models.FileField(upload_to = get_photo_path)
	def __unicode__(self):
		return self.username
