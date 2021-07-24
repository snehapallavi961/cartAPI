from django.db import models

# Create your models here.
class shoppingcart(models.Model):
    fullname = models.CharField(max_length=100)
    item = models.CharField(max_length=20)
    price = models.CharField(max_length=15)
    discount = models.CharField(max_length=30)
    quantity = models.CharField(max_length=45)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE