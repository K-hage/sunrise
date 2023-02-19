from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveUpdateAPIView

from .models import Company, Product, Contacts
from .permissions import CompanyEmployeesPermissions
from .serializers import ProviderSerializers, ProviderUpdateSerializers, ProductSerializer, ContactsSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    default_serializer = ProviderSerializers
    serializer_classes = {
        'update': ProviderUpdateSerializers,
        'partial_update': ProviderUpdateSerializers,
    }
    permission_classes = [CompanyEmployeesPermissions]
    ordering = ['id']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]
    filterset_fields = ['contacts__country']

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def perform_destroy(self, instance):
        contacts = instance.contacts
        super().perform_destroy(instance)
        contacts.delete()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [CompanyEmployeesPermissions]
    ordering = ['id']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]


class ContactsRUAPIView(RetrieveUpdateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [CompanyEmployeesPermissions]
    ordering = ['id']
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter
    ]
