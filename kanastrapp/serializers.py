from rest_framework import serializers 
from .models import Person 

class PersonSerializer(serializers.ModelSerializer):
    debtDueDate = serializers.DateField(input_formats=['%d/%m/%Y'])
    class Meta:
        model = Person
        fields = ['name', 'governmentId', 'email', 'debtAmount', 'debtDueDate']