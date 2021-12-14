import datetime 

from django.db import models
from django.db.models.fields import EmailField

class Owners(models.Model):
    owner_name = models.CharField(max_length=45, blank=False, null=False)
    email = models.EmailField(max_length=200)
    age = models.PositiveIntegerField(blank=False, null=False)

    # def __str__(self):
    #     return self.owner_name
    
    # meta 사용해서 테이블명 수정
    # class Meta:
    #     db_table = 'owners'

class Dogs(models.Model):
    dog_name = models.CharField(max_length=45, blank=False, null=False)
    age = models.PositiveIntegerField(blank=False, null=False)
    owners = models.ForeignKey('Owners', on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.dog_name

