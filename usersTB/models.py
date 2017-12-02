from django.db import models



class Users(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    email_id = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=30, blank=False)
    pwd = models.CharField(max_length=100, blank=False)


    def __unicode__(self):
        return self.pwd
