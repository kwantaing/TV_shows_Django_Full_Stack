from __future__ import unicode_literals
from datetime import datetime
from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self,postData,create=False):
        now = datetime.now()
        now = now.strftime("%Y-%m-%d")
        isValid = True
        errors={}
        if len(postData["title"]) < 2:
            errors["title"] = "Title should be at least 2 characters"
            isValid = False
        if create == True:
            if Show.objects.filter(title = postData["title"]):
                errors["title1"] = "Title already exists in database"
                isValid = False
            else:
                print("new show")
        if len(postData["network"]) < 3:
            errors["network"] = "Network should be at least 3 characters"
            isValid = False
        if len(postData["description"])<10:
            if(len(postData["description"])==0):
                isValid = True
            else:
                errors["description"] = "Description should be at least 10 characters"
                isValid = False
        if postData["release_date"]> now:
            errors["release_date"] = "Release Date should be in the past"
            isValid = False

        return errors
# Create your models here.

class Show(models.Model):
    title=models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date=models.DateField()
    description = models.TextField()
    objects = ShowManager()

    def __str__(self):
        return f"{self.title}"


