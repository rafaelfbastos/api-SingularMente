from rest_framework import serializers
from .models import *


class PillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pills
        fields = '__all__'


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['number']


class ContactsSerializer(serializers.ModelSerializer):
    numbers = PhonesSerializer(many=True, read_only=True, source='phones_set')

    class Meta:
        model = Contacts
        fields = ['id', 'name', 'address', 'description', 'latitude', 'longitude', "numbers"]


class InformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'
