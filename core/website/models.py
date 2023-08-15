from django.db import models

# Create your models here.

class NewsLetter(models.Model):
    """This class consists newsletter fields"""
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.email
    
    # Capitalize name and make email to lowercase
    def clean(self):
        self.name = self.name.capitalize()
        self.email = self.email.lower()


class Contact(models.Model):
    """This class consists contacts fields"""
    name = models.CharField(max_length=250)
    email =models.EmailField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email
    
    # Capitalize name and make email to lowercase
    def clean(self):
        self.name = self.name.capitalize()
        self.email = self.email.lower()
