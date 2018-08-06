#accounts/models.py
from django.db import models
from django.conf import settings


class Profile(models.Model):
   
   user = models.OneToOneField(settings.AUTH_USER_MODEL) #best!!
   phone_number = models.CharField(max_length =20)
   email = models.EmailField()
   index = models.CharField(max_length =20,default=0)#어디까지 정제를 했는지
   allocated = models.CharField(max_length =50)# 몇문장이 일감으로 할당 되었고






   
