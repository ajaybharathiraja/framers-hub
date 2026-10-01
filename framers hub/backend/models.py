from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = (
        ('farmer', 'Farmer'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    objects = CustomUserManager()

class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer_profile')
    phone = models.CharField(max_length=15, blank=True)
    state = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=255, blank=True)
    farming_information = models.TextField(blank=True)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    phone = models.CharField(max_length=15, blank=True)
    delivery_information = models.TextField(blank=True)


class Product(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='products')
    commodity = models.CharField(max_length=100)
    variety = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=50, blank=True)


class Product(models.Model):
    farmer = models.ForeignKey(FarmerProfile, on_delete=models.CASCADE, related_name='products')
    commodity = models.CharField(max_length=100)
    variety = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    harvest_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Listing(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='listing')
    selling_price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_listing = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ai_predicted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="AI estimated price at the time of prediction")
    reference_market_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Benchmark market price for the commodity/date")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    is_primary = models.BooleanField(default=False)

class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='inventory')
    total_quantity = models.DecimalField(max_digits=12, decimal_places=2)
    reserved_quantity = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    available_quantity = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.available_quantity = self.total_quantity - self.reserved_quantity
        super().save(*args, **kwargs)

class Cart(models.Model):
    customer = models.OneToOneField(CustomerProfile, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def subtotal(self):
        return self.quantity * self.listing.selling_price_per_kg

class Order(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('PROCESSING', 'Processing'),
        ('READY/SHIPPED', 'Ready/Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    )
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('REFUNDED', 'Refunded'),
    )
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='CREATED')
    provider = models.CharField(max_length=50, default='TEST_MODE')
    payment_timestamp = models.DateTimeField(null=True, blank=True)
    verification_status = models.BooleanField(default=False)


class ResearchEvent(models.Model):
    EVENT_TYPES = (
        ('USER_REGISTERED', 'User Registered'),
        ('LOGIN', 'Login'),
        ('PRODUCT_VIEWED', 'Product Viewed'),
        ('PRODUCT_LISTED', 'Product Listed'),
        ('MARKET_PRICE_VIEWED', 'Market Price Viewed'),
        ('PRICE_PREDICTION_REQUESTED', 'Price Prediction Requested'),
        ('CROP_RECOMMENDATION_REQUESTED', 'Crop Recommendation Requested'),
        ('CROP_RECOMMENDATION_VIEWED', 'Crop Recommendation Viewed'),
        ('PRODUCT_ADDED_TO_CART', 'Product Added to Cart'),
        ('CHECKOUT_STARTED', 'Checkout Started'),
        ('ORDER_CREATED', 'Order Created'),
        ('PAYMENT_SUCCESS', 'Payment Success'),
        ('ORDER_COMPLETED', 'Order Completed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    metadata = models.JSONField(default=dict, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class TAMSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tam_surveys')
    perceived_usefulness = models.IntegerField(help_text="Rating from 1-5 on Perceived Usefulness")
    perceived_ease_of_use = models.IntegerField(help_text="Rating from 1-5 on Perceived Ease of Use")
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
