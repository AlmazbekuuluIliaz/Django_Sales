from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination




class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['email','first_name','last_name', 'telephone']
    ordering_fields = ['first_name', 'email', 'telephone']
    filterset_fields = ['first_name', 'email','telephone']


class MainViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['sale','number']
    ordering_fields = ['code_company', 'code_sale', 'sale_date']
    filterset_fields = ['code_company', 'code_sale','sale_date']


class ContactViewSet(ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['first_name','last_name', 'position', 'address']
    ordering_fields = ['birthday']


class CompaniesViewSet(ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['code_company']


class SalesPagination(PageNumberPagination):
    page_size = 5
    page_sizer_query_param = 'paginate_by'
    max_page_size = 10


class SaleViewSet(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    pagination_class = SalesPagination
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name','company','code_sale']
    ordering_fields = ['price', 'number_storage', 'number','code_sale']
    filterset_fields = ['price', 'number_storage', 'number','code_sale']
    @action(methods=['Delete'], detail=True, url_path='delete') 
    def del_sale(self,request, pk=None):
        sale=self.queryset.get(id=pk)
        sale.delete()
        return Response('Акция была удалена')
    @action(methods=['Post'], detail=False, url_path='post') 
    def post_sale(self,request, pk=None):
        title=self.queryset.create(name=request.data.get('name'))
        title.save()
        return Response('Акция была создана')
    @action(methods=['GET'], detail=False,url_path='get')
    def get_data(self, request, **kwargs):
        sales = Sales.objects.all()
        return Response({'sales': [sale.name for sale in sales]})



class StorageViewSet(ModelViewSet):
    queryset = Storages.objects.all()
    serializer_class = StoragesSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['phone', 'address', 'boss']
    ordering_fields = ['phone', 'number_storage']
    filterset_fields = ['phone', 'number_storage']


class GetSaleView(ListAPIView):
    queryset = Sales.objects.filter(Q(price__lte=1000)&Q(number__lte=100000))
    serializer_class = SalesSerializer
    pagination_class = SalesPagination
    search_fields = ['name','company','code_sale']
    ordering_fields = ['price', 'number_storage', 'number','code_sale']
    filterset_fields = ['price', 'number_storage', 'number','code_sale']

    

class GetCompaniesView(ListAPIView):
    queryset = Companies.objects.order_by('-name')
    serializer_class = CompaniesSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    search_fields = ['name', 'address']
    ordering_fields = ['code_company']





