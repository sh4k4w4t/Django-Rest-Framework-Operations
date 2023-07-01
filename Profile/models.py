from django.db import models

class IndiviadualUserModel(models.Model):
    id= models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age  = models.IntegerField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name