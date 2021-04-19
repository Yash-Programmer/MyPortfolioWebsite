from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000)
     
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

     