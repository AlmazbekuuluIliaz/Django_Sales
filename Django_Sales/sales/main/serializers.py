from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'first_name', 'email', 'last_name', 'telephone', 'is_active', 'is_staff', 'is_superuser']


class MainSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Main
        fields = ['url', 'sale', 'number', 'code_company', 'code_sale', 'sale_date', 'artist']


class ContactsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Contacts
        fields = ['url', 'code_assistant', 'first_name', 'last_name', 'birthday', 'address', 'phone', 'position', 'code_company']


class CompaniesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Companies
        fields = ['url', 'name', 'address', 'phone', 'code_company']


class SalesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sales
        fields = ['url', 'name', 'company', 'price', 'number_storage', 'number', 'photo', 'description', 'code_sale']


class StoragesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Storages
        fields = ['url', 'phone', 'address', 'boss', 'number_storage']