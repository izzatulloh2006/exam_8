from django.http import HttpResponse
from django.urls import path
from apps.utils import send_email
from apps.views import EmailView
from .views import CategoryListView, ProductListView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterCreateAPIView

def send_email_task(req):
    return HttpResponse(send_email('Xabar', 'Izzatulloh', ['fayzullaxojaevi@gmail.com']).get('message'))

urlpatterns = [

    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    # path('notify/', new_products, name='notify-new-products'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    # path('register/', RegisterView.as_view(), name='register'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('categories/', CategoryListView.as_view(), name='category-list'),
    # path('products/', ProductListView.as_view(), name='product-list'),

]







