from django.db import models
from django.utils import timezone
import uuid
# Create your models here.


class Customer():
    customer_id = models.UUIDField(primary_key=True, default=str(uuid.uuid4()))
    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(blank=False)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False)
    auth_token = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.username


class Vendor(models.Model):
    vendor_id = models.UUIDField(primary_key=True)
    vendor_name = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=200)
    vendor_email = models.EmailField()
    vendor_phone_number = models.CharField(max_length=10)
    vendor_gst_number = models.CharField(max_length=15)
    vendor_account_number = models.CharField(max_length=20)
    vendor_pincode = models.CharField(max_length=6)


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True)
    category_name = models.CharField()


class Product(models.Model):
    product_id = models.UUIDField(primary_key=True)
    product_name = models.CharField(max_length=200)
    product_price = models.PositiveIntegerField()
    product_description = models.CharField(max_length=2000)
    rating = models.IntegerField()
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)


class Address(models.Model):
    address_id = models.UUIDField(primary_key=True)
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=30)
    pincode = models.PositiveIntegerField(max_length=6)
    address = models.CharField()


class Cart(models.Model):
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class WishList(models.Model):
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    order_id = models.IntegerField()
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ManyToManyField(Product)
    amount = models.FloatField()
    discount = models.FloatField()
    order_status = models.CharField(max_length=100)
    # k = models.CompositePrimaryKey("Customer_id", "product_id")


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True)
    description = models.TextField()
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Product_Image(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField()
    image_id = models.UUIDField(primary_key=True)


class Review_Images(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    iamge_url = models.URLField()
    image_id = models.UUIDField(primary_key=True)
