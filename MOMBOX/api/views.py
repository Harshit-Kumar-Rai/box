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
        "Msg" : "Data added secesfully",
        "RESULT" : 1,
        
      }
      return Response(serialzer.data, msg)
    else:
      return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FilteredAPIView(APIView):
  
  def get(self, request, pk):
    
    try:
      data = Master.objects.get(id=pk)
    
    except Master.DoesNotExist:
       return Response({"Msg":"Invalid ID",
                        "Result": 0})
      
    serializer = MasterDataSerialzer(data)
    return Response(serializer.data)
  
  def delete(self, request, pk):
    
    try:
      data = Master.objects.get(id=pk)
    except Master.DoesNotExist:
      return Response({'Result' : 0, "Msg" : "Invalid id"})
    data.delete()
    return Response({"Result":1,"Msg": "Data Deleted"})
    
  def put(self, request, pk):
    
    try:
      data = Master.objects.get(id=pk)
    except  Master.DoesNotExist:
      return Response({'Msg' : "User Not Exists"})
    
    serialzer = MasterDataSerialzer(data,request.data)
    if serialzer.is_valid():
      serialzer.save()
      return Response({"Msg" : "User Updated"})
    else:
      return Response({'Msg':"Invalid Details"})
    