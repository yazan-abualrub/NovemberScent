from django.db import models
from django.contrib.auth.models import User
from scents.models import Product
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_fav = models.ManyToManyField(Product)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.user.username
    
    USERNAME_FIELD = 'email'

    
    
    