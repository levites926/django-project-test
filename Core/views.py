from . import models
from django.shortcuts import render

def uploadFile(request):
	if request.method == "POST":
	#fetching the form data
		fileTitle = request.POST["fileTitle"]
		uploadedFile = request.FILES["uploadedFile"]

		#saving the information in the database
		document = models.Document(
			title = fileTitle,
			uploadedFile = uploadedFile
		)
		document.save()

	documents = models.Document.objects.all()

	return render(request, "Core/upload-file.html", context = { "files": documents})

# Create your views here.
