from django.urls import  path
from actors.views import ActoCreateListView, ActorRetriveUpdateDestroyView


urlpatterns = [
    path('', ActoCreateListView.as_view(), name='actor_create_List_view'),
    path('<int:pk>/', ActorRetriveUpdateDestroyView.as_view(), name='actor_retrive_update_destroy_view'),
]


