from django.db import models

class User(models.Model):
    user_id = models.Autofield
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    Email_id = models.CharField(max_length=50)


    