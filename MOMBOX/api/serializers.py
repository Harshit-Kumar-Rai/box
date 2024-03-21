from rest_framework import serializers
from .models import Master

class MasterDataSerialzer(serializers.ModelSerializer):
  class Meta:
    model = Master
    fields = '__all__'
