from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile of {self.user.username}'


"""
In Object-Relational Mapping (ORM), a OneToOneField relationship is a type of 
relationship between two database tables where each record in one table 
is associated with exactly one record in the other table. In Django's ORM, 
OneToOneField is a field type used to define such relationships between models.
"""