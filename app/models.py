"""
Definition of models.
"""

from django.db import models

# Create your models here.
class User(models.Model):
    user_ID = models.BigAutoField()
    city_ID = models.AutoField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=120)
    zip_code = models.IntegerField()
    phone_number = models.CharField(max_lenght = 30)
    e_mail = models.EmailField(max_length=60)

class User_role(models.Model):
    user_ID = models.IntegerField()
    role_ID = models.IntegerField()
    user_in_role = models.IntegerField()
    roll_start_date = models.DateField(auto_now=False, auto_now_add=True)

class Role(models.Model):
    role_ID = models.BigAutoField()
    role_name = models.CharField(max_lenght = 30)

class City(models.Model):
    city_ID = models.AutoField()
    city_name = models.CharField(max_lenght = 30)

class Country(models.Model):
    country_ID = models.AutoField()
    country_name = models.CharField(max_lenght = 30)

class Course(models.Model):
    course_ID = models.BigAutoField()
    category = models.BigIntegerField()
    sub_catergory = models.BigIntegerField()
    user_ID = models.BigIntegerField()
    course_name = models.CharField(max_lenght = 60)
    course_description = models.SlugField(max_lenght = 500)
    course_contents = models.SlugField(max_lenght = 500)
    course_fee = models.BooleanField()
    course_price = models.FloatField()

class Banking_card(models.Model):
    card_ID = models.BigAutoField()
    user_ID = models.BigIntegerField()
    card_number = models.IntegerField()
    card_CVC = models.IntegerField()
    card_owner_first_name = models.CharField(max_lenght = 30)
    card_owner_last_name = models.CharField(max_lenght = 30)
    card_due_date = models.DateField()