from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class PasswordList(models.Model):
    # password_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    password_name = models.CharField(max_length=100)
    password_username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.password_name

    def get_absolute_url(self): 
       return reverse('password_name', args=[str(self.user)])
