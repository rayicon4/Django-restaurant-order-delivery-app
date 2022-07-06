from django.db import models
from django import forms
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from datetime import datetime
from django.contrib.auth.models import User

from django.db.models import F

#the custom user model manager
class MyAccountManager(BaseUserManager):


    def create_user(self, username, firstname, lastname, email, phonenumber, location, password=None):
        if not username:
            raise ValueError("Users must have a username")
        if not email:
            raise ValueError("Users must have a valid email address")
        user = self.model(
            username = username,
            firstname = firstname,
            lastname=lastname,
            email = self.normalize_email(email),
            phonenumber=phonenumber,
            location=location,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, username, firstname, lastname, email, phonenumber, location, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            phonenumber=phonenumber,
            location=location,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



#we are building a custom form with a custom backkend

class customerinfomodel(AbstractBaseUser):
    username = models.CharField(verbose_name="username", max_length=30, unique=True)
    firstname = models.CharField(verbose_name="first name", max_length=50)
    lastname = models.CharField(verbose_name="last name", max_length=50)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    phonenumber = models.IntegerField(verbose_name="phone number", unique=True)
    location = models.CharField(verbose_name="location",max_length=300)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    #the below fields are required when creating a custom model
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'email', 'phonenumber', 'location']

    def __str__(self):
        return self.username

    #the line below checks to se if the user has permission to do admin stuff
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True



class morningmenu(models.Model): ##MORNING
    food_type = models.CharField(max_length = 100)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1, null=True)
    description = models.TextField(default='', max_length=100)
    created = models.DateTimeField(default=datetime.now())
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.food_type

    @property
    def qtyprice(self):
        total = self.price * self.quantity
        return total

    


class afternoonmenu(models.Model): ##AFTERNOON
    food_typea = models.CharField(max_length = 100)
    pricea = models.CharField(max_length=20)
    descriptiona = models.TextField(default='', max_length=100)
    createda = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.food_typea


class eveningmenu(models.Model): ##EVENING
    food_types = models.CharField(max_length = 100)
    prices = models.CharField(max_length=20)
    descriptions = models.TextField(default='', max_length=100)
    createds = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.food_types

class orderinfo(models.Model):
    order = models.ForeignKey(morningmenu, on_delete=models.CASCADE, default=False)
    created = models.DateTimeField(default=datetime.now())
    # food_type = models.CharField(max_length=100)
    # price = models.CharField(max_length=20)
    # qantity = models.IntegerField(default=2)

    #def __str__(self):
        #return f'{self.order} - {self.price}'

