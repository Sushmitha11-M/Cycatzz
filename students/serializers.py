from rest_framework import serializers

from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'Student_id',
            'Name',
            'DateofBirth',
            'Branch',
            'Email_address',
            'Phone_number'
        ]