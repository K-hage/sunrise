from django.db import transaction
from rest_framework import serializers

from corp.models import Company, Product, Contacts


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ProviderSerializers(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(required=False)

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = (
            'id',
            'debt',
            'pub_date',
        )

    @transaction.atomic
    def create(self, validated_data):
        contacts = validated_data.pop('contacts')
        c = Contacts.objects.create(**contacts)
        provider = Company.objects.create(contacts=c, **validated_data)
        return provider


class ProviderUpdateSerializers(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    contacts = ContactsSerializer(read_only=True)

    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = (
            'id',
            'debt',
            'pub_date',
        )
