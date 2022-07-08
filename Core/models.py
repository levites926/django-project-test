from django.db import models

class Document(models.Model):
	title = models.CharField(max_length = 200)
uploadedFIle = models.FileField(upload_to = "Uploaded Files/")
dateTimeOfUpload = models.DateTimeField(auto_now = True)
# Create your models here.
