

from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
 

    class meta:
        db_table = 'tbl_users'

class Products(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=200)
    prod_category = models.CharField(max_length=200)
    prod_cost = models.FloatField()

    class meta: 
        db_table = 'tbl_products'
