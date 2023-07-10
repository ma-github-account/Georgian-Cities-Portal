from .models import Place, Category
from .serializers import CategorySerializer, PlaceSerializer
from rest_framework import generics

from django.http import Http404
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404


# Create your views here.
class CategoryList(generics.ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  name = 'category-list'

class CategoryDetail(generics.RetrieveAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  name = 'category-detail'


class PlaceList(generics.ListAPIView):
  queryset = Place.objects.filter(active=True)
  serializer_class = PlaceSerializer
  name = 'places-list'
  

class PlaceDetail(generics.RetrieveAPIView):
  queryset = Place.objects.filter(active=True)
  serializer_class = PlaceSerializer
  name = 'places-detail'
  