
from django.urls import path
from genres.views import GenreCreateListView, GenreRetriveUpdteDestroy


urlpatterns = [
    path('', GenreCreateListView.as_view(), name='genre_create_list_view'),
    path('<int:pk>/', GenreRetriveUpdteDestroy.as_view(), name='genre_detail_view')
]
