from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null=True)
    name = models.CharField(max_length=150)
    company = models.CharField(max_length=150 )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=150, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to = 'img/%Y/%m/%d/')
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now)

    
    def __str__(self) :
        return self.name
      
    class Meta:
        ordering = ["-publish_date"]
        
