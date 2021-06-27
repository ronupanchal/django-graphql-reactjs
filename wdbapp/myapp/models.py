from django.db import models

# Create your models here.


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s" %(self.first_name) 


class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s" %(self.category_name) 

class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return "%s" %(self.product_name)

