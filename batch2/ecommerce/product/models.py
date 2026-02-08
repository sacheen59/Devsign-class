from django.db import models
from product.form_validation import validate_less_than_0

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['id']

    def __str__(self):
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2,validators=[validate_less_than_0])
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products', blank=True, null=True)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class LoginPractise(models.Model):
    email = models.EmailField()
    password = models.CharField()
    is_Admin = models.BooleanField(default=True)

    def __str__(self):
        return self.email