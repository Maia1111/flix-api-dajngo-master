
from django.urls import path
from . import views

urlpatterns = [
    path('', views.genre_create_list_view, name='genre_create_list_view'),
    path('<int:pk>/', views.genre_detail_view, name='genre_detail_view'),

]
