from rest_framework import serializers
from users.models import (Students,Orders)

class Studentsserializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__' 

class Ordersserializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

class Deleteserializers(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'  

class StudentsAddressserializers(serializers.ModelSerializer):
    class Meta:
        model = 
        fields = '__all__'

class StudentsDetailsAddressSerializers(serializers.ModelSerilizer):
    students_address = StudentsAddressSerializers(many=True)
