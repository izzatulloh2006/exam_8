from django.shortcuts import redirect
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework import status
from django.views.generic import FormView
from apps.models import User
from apps.serializers import UserModelSerializer, RegisterModelSerializer, CategoryModelSerializer, ProductSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Category, Product
from .serializers import CategoryModelSerializer, ProductSerializer
from django.core.mail import send_mail
from datetime import datetime
from rest_framework.pagination import PageNumberPagination


class RegisterCreateAPIView(CreateAPIView):
        queryset = User.objects.all()
        serializer_class = RegisterModelSerializer



class ProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryModelSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset





class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category', None)
        search_term = self.request.query_params.get('search', None)

        if category_name:
            queryset = queryset.filter(category__name=category_name)

        if search_term:
            queryset = queryset.filter(name__icontains=search_term) | queryset.filter(description__icontains=search_term)

        return queryset




class EmailView(FormView):
    success_url = '.'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('.', self.get_context_data(form=form))