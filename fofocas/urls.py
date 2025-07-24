from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fofocas, name='lista_fofocas'),
    path('nova/', views.nova_fofoca, name='nova_fofoca'),
    path('votar/<int:fofoca_id>/<str:tipo>/', views.votar, name='votar'),
]