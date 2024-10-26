from django.shortcuts import render
from django.http import JsonResponse
from .models import Genre
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import generics


@csrf_exempt
def genre_create_list_view(request):    
    if request.method == 'GET':
        genres = Genre.objects.all()
        data = [{'id': genre.id, 'name': genre.name} for genre in genres]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            new_genre = Genre(name=data['name'])
            new_genre.save()
            return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
def genre_detail_view(request, pk):
    genre = get_object_or_404(Genre, id=pk)

    if request.method == 'GET':
        data = {'id': genre.id, 'name': genre.name}
        return JsonResponse(data, safe=False)

    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'id': genre.id, 'name': genre.name}, status=200)
    
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Genre deleted successfully'}, status=204)
  