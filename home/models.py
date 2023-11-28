from django.db import models 


class User_Info(models.Model):
    mail = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to="FILES")