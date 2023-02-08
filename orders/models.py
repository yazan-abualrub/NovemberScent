from django.db import models
from django.contrib.auth.models import User
from scents.models import Product
from datetime import datetime



class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    OrderDate = models.DateTimeField(default=datetime.now)
    details = models.ManyToManyField(Product, through='OrderDetails')
    is_finished = models.BooleanField()
    
    def __str__(self):
        return 'Order:' + str(self.id)
    
class OrderDetails(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return 'OrderDetails:' + self.product.name
    
    class Meta:
        ordering = ['-id']
        
        
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ShipAddress = models.CharField(max_length=150)
    ShipPhone = models.CharField(max_length=50)


        
