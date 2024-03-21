from django.db import models

class Master(models.Model):
  
  mac_id = models.CharField(max_length=100)
  name = models.CharField(max_length=180)
  email = models.EmailField()
  contact = models.CharField(max_length=13)
  
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=120)
  pincode = models.CharField(max_length=6)
  state = models.CharField(max_length=50)
  
  
  def __str__(self):
    return self.name
  
  