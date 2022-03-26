from pyexpat import model
from typing import ChainMap
from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=5000)
    comment = models.TextField()
     
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(default="None")

    def __str__(self):
        return self.name

class Skill(models.Model):
    technology =models.CharField(max_length=100)
    languages = models.CharField(max_length=1000)
    description = models.TextField()

    def __str__(self):
        return self.technology

class Project(models.Model):
    name = models.CharField(max_length=100000)
    repo_href = models.CharField(max_length=1000)
    src = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.name

class Upload(models.Model):
    name = models.CharField(max_length=1000)
    desc = models.TextField()
    upload = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.name

# class Certification_6(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
#
# class Certification_5(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
# class Certification_4(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
# class Certification_3(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
# class Certification_2(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
# class Certification_1(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name
# class Certification_LKG(models.Model):
#     name = models.CharField(max_length=1000000)
#     certificate_id = models.CharField(max_length=1000000, blank=True, default='Not Provided')
#     file = models.FileField(null=True, blank=True)

#     def __str__(self):
#         return self.name

# class Trophy(models.Model):
#     name = models.CharField(max_length=10000)
#     file = models.FileField(null=True, blank=True)
#     def __str__(self):
#         return self.name

# class Medal(models.Model):
#     name = models.CharField(max_length=10000,null=True, blank=True)
#     organization = models.CharField(max_length=1000,null=True, blank=True)
#     STD = models.CharField(max_length=1000,null=True, blank=True)
#     front_side = models.FileField(null=True, blank=True)
#     back_side = models.FileField(null=True, blank=True)
    

#     def __str__(self):
#         return self.name

    

     