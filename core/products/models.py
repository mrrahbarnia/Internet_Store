from django.db import models
from django.contrib.contenttypes.fields import (
    GenericRelation, GenericForeignKey
    )
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

SITUATION = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved')
)

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
    discount_Percentage = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    style = models.ForeignKey("Styles",on_delete=models.SET_NULL, null=True)
    approved = models.CharField(max_length=50,null=True,choices=SITUATION,default='Pending')
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    
    def get_absolute_url(self):
        return reverse("products:men-single", kwargs={"men_product":self.model_name})
    
class WomanProducts(models.Model):
    """
    These are attributes of women products 
    """
    model_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Women_Products", default="products/Women_Products/women.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_Percentage = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    style = models.ForeignKey("Styles",on_delete=models.SET_NULL, null=True)
    approved = models.CharField(max_length=50,null=True,choices=SITUATION,default='Pending')
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    
    def get_absolute_url(self):
        return reverse("products:women-single", kwargs={"women_product":self.model_name})

class KidProducts(models.Model):
    """
    These are attributes of kids products 
    """
    model_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Kid_Products", default="products/Kid_Products/kid.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_Percentage = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    style = models.ForeignKey("Styles",on_delete=models.SET_NULL, null=True)
    approved = models.CharField(max_length=50,null=True,choices=SITUATION,default='Pending')
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    
    def get_absolute_url(self):
        return reverse("products:kids-single", kwargs={"kids_product":self.model_name})
    

class Accessories(models.Model):
    """
    These are attributes of accessories products 
    """
    model_name = models.CharField(max_length=255)
    introduction = models.TextField()
    image = models.ImageField(upload_to="products/Accessories", default="products/Accessories/kid.jpg")
    advertiser = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discount_Percentage = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    comments = GenericRelation("Comment")
    approved = models.CharField(max_length=50,null=True,choices=SITUATION,default='Pending')
    counted_views = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.model_name
    
    def get_absolute_url(self):
        return reverse("products:accessories-single", kwargs={"accessory":self.model_name})
    

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
    approved = models.CharField(max_length=50,null=True,choices=SITUATION,default='Pending')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.email



    
