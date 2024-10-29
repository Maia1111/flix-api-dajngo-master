from django.shortcuts import render
from rest_framework import generics
from actors.models import  Actor
from actors.serializers import ActorSerializer




class ActoCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class ActorRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer