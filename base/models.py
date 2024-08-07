from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    address = models.CharField()
    email = models.EmailField()
    # phone = models.PhoneNumberField(blank=True)