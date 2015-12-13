from django.db import models

class Library(models.Model):
	libraryName=models.CharField(max_length=100,unique=True)

	def __str__(self):
		return self.libraryName

class Books(models.Model): #Books is a Django Model, so Django knows that it should be saved in the database.
	bookName=models.CharField(max_length=100)
	library=models.ForeignKey(Library,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.bookName

