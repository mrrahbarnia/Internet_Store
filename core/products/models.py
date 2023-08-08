from django.db import models
from django.contrib.contenttypes.fields import (
    GenericRelation, GenericForeignKey
    )
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class MenProducts(models.Model):
    """
    These are attributes of women products 
    """
    model_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Men_Products", default="products/Men_Products/men.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    style = models.ForeignKey("Styles",on_delete=models.SET_NULL, null=True)
    approved = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    
class WomanProducts(models.Model):
    """
    These are attributes of women products 
    """
    model_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Women_Products", default="products/Women_Products/women.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    style = models.ForeignKey("Styles",on_delete=models.SET_NULL, null=True)
    approved = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    

class KidProducts(models.Model):
    """
    These are attributes of kids products 
    """
    model_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Kid_Products", default="products/Kid_Products/kid.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    style = models.ForeignKey("Styles",on_delete=models.SET_NULL, null=True)
    approved = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    

class Accessories(models.Model):
    """
    These are attributes of accessories products 
    """
    accessory_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Accessories", default="products/Accessories/kid.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    approved = models.BooleanField(default=False)
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.accessory_name
    

class Styles(models.Model):
    style_name = models.CharField(max_length=255)

    def __str__(self):
        return self.style_name


class Comment(models.Model):
    """
    This class used for comments of products
    """
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    email = models.EmailField()
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.email



    
