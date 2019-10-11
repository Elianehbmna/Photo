# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt

class Location(models.Model):
    location_name=models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.delete()

class Category(models.Model):
    category_name=models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def update_category(self):
        self.delete()





# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location,db_column='location_name', blank=True)
    category = models.ForeignKey(Category,db_column='category_name', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.name

    def save_image(self):
        self.save()
    
    # @classmethod
    # def delete_image(cls,id):
    #     images = cls.objects.filter(id=id)
    #     images.delete()
    
    # def get_image_by_id(id):
    #     images = cls.objects.filter(id=id)
    #     return images

    # def filter_by_location(location):
    #     images = cls.objects.filter(location=location)
    #     return images
    @classmethod
    def todays_image(cls):
        today = dt.date.today()
        image = cls.objects.filter(pub_date__date = today)
        return image
        
    @classmethod
    def days_image(cls,date):
        image = cls.objects.filter(pub_date__date = date)
        return image

    @classmethod
    def search_by_image(cls,search_term):
        image = cls.objects.filter(category__category_name__contains=search_term)
        return image
