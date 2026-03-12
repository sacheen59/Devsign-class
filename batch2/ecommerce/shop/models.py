from django.db import models
from django.contrib.auth.models import User
from product.models import Product


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} => {self.product}"


class Order(models.Model):
    PAYMENT_STATUS = (
        ('paid','Paid'),
        ('unpaid', 'Unpaid')
    )
    PAYMENT_METHOD = (
        ('COD', 'Cash on Delivery'),
        ('esewa', 'Esewa'),
        ('khalti', 'Khalti')
    )
    DELIVERY_STATUS = (
        ('pending', 'Pending'),
        ('delivered','Delivered'),
        ('failed','Failed')
    )
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=10, default='unpaid')
    payment_method = models.CharField(choices=PAYMENT_METHOD, max_length=20, default='COD')
    delivery_status = models.CharField(choices=DELIVERY_STATUS, max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} => {self.product.product_name}'
