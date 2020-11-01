from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_validity(self):
        if (self.date_of_birth == None or self.state == None
            or self.city == None or self.district == None
            or self.zip_code == None or self.user.first_name == ''
            or self.user.last_name == ''):
            return False
        else:
            return True
        