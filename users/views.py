from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import*
from users.serializers import*

class GetStudentsView(APIView):

    def get(self,request):
        print("req ",request.GET)
        name = request.GET.get("myname")
        print("name ",name)
        if name:
            instance = Students.objects.filter ( first_name = name )

        else:
            instance = Students.objects.all()
        ser = Studentsserializers(instance,many=True)
        return Response(ser.data)
    
    def post(self,request):

        params = request.data
        print("params",params)

        serializers = Studentsserializers(data = params)
        serializers.is_valid(raise_exception = True)
        serializers.save()

        return Response({"message","Done! "})
    

class GetOrdersViews(APIView):

    def get(self,request):
        print("req ",request.GET)
        name = request.GET.get("myname")
        print("name ",name)
        if name:
            instance = Orders.objects.filter ( order_name = name )
        else:
            instance = Orders.objects.all()
        serializer = Ordersserializers(instance,many=True)
        return Response(serializer.data)
        

    def post(self,request):

        params = request.data
        print("params-----",params)

        serializer = Ordersserializers(data = params)
        if serializer.is_valid():
            serializer.save()
            return Response({"Order":"placed! "})
        else:
            print("error",serializer.errors)
            return Response({"Error":str(serializer.errors)})
        

class DeleteStudentViews(APIView):
    def get (self,request,pk):
        instance = Students.objects.get(id=pk)
        instance.delete()

        return Response({"Data","deleted"})
    
class StudentsDetailsAddresss(APIView):
    def get(self,request,pk):
        instance = Students.objects.filter(id=pk)
        serializers = StudentDetailsAddressserializers(instance,many=True)
        return Response(serializers.data)

