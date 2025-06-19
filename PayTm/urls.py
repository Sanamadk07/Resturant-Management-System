from django.urls import path
from . import views

urlpatterns = [
    path('esewa/', views.pay_with_esewa, name='pay_with_esewa'),
    path('esewa/success/', views.esewa_success, name='esewa_success'),
    path('esewa/failure/', views.esewa_failure, name='esewa_failure'),
]
