from django.contrib.auth.hashers import make_password
from django.db.models import Model
from django.db.models import CharField, IntegerField, TextField, ForeignKey, EmailField, CASCADE, ImageField
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer


class User(AbstractUser):
    pass



class Category(Model):
    name = CharField(max_length=100)
    description = TextField()

    def __str__(self):
        return self.name

class Product(Model):
    name = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to='products/')
    owner = ForeignKey(User, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)

    def __str__(self):
        return self.name


