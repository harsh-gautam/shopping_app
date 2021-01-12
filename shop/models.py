from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True) # product id
    product_name = models.CharField(max_length=100) # product  name
    product_desc = models.CharField(max_length=2000) # product description
    product_pub = models.DateField() # product published date
    category = models.CharField(max_length=50, default="") # product category
    sub_category = models.CharField(max_length=50, default="") # product sub-category
    image = models.ImageField(upload_to="shop/images", default="") # product image
    price = models.IntegerField(default=0) # product price
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0) # product rating
    discount = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipcode = models.IntegerField(default=0)
    payment_mode = models.CharField(max_length=10)
    itemsjson = models.CharField(max_length=300)
    totalprice = models.IntegerField(default=0)
    updates = models.CharField(max_length=5000, default="")
 