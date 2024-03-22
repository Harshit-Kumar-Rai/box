from django.shortcuts import render
from .models import Master
from .serializers import MasterDataSerialzer
from rest_framework import status
from rest_framework.views import  APIView
from rest_framework.response import Response

class MasterAPIView(APIView):
  
  def get(self, request):
    data = Master.objects.all()
    serializer = MasterDataSerialzer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serialzer = MasterDataSerialzer(data=request.data)
    if serialzer.is_valid():
      serialzer.save()
      msg  ={
        "ERROR" : "Data added secesfully",
        "RESULT" : 1,
        
      }
      return Response(serialzer.data, msg)
    else:
      return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)