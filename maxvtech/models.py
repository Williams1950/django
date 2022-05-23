from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Destination2(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

class Dest(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class slider(models.Model):
    home_title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.home_title


#img = models.ImageField(upload_to='pics')

class feature(models.Model):
    top_title = models.CharField(max_length=100)
    top_desc = models.CharField(max_length=100)
    img = models.FileField(upload_to="pics/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])

    def __str__(self):
        return self.top_title

class testimonials(models.Model):
    top_desc = models.CharField(max_length=100)
    top_name = models.CharField(max_length=100)
    top_job = models.CharField(max_length=100)

    def __str__(self):
        return self.top_name

class testimonialTop(models.Model):
    top_desc1 = models.CharField(max_length=100)
    top_name2 = models.CharField(max_length=100)
    img = models.FileField(upload_to="pics/%Y/%m/", validators=[FileExtensionValidator(['pdf','png','jpeg','jpg', 'doc', 'svg'])])

    def __str__(self):
        return self.top_name2
