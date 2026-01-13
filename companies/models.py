from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logos")

    type = models.CharField(max_length=100)

    about_company = models.TextField()

    work_space = models.TextField()
    website = models.URLField(max_length=200, blank=True, null=True)