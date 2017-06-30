# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Max, Count

from rest_framework import generics
from rPlaceApp.models import Tile, CanPlace
from rPlaceApp.serializers import TileSerializer, UserSerializer, CanPlaceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers

# Create your views here.

class TileList(generics.ListCreateAPIView) :
	queryset = Tile.objects.all()
	serializer_class = TileSerializer
	def perform_create(self, serializer) :
		serializer.save(owner = self.request.user)

class TileDetail(generics.RetrieveUpdateAPIView) :
	queryset = Tile.objects.all()
	serializer_class = TileSerializer

class UserList(generics.ListAPIView) :
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def perform_create(self, serializer) :
		canPlace = CanPlace()
		canPlace.user = self
		canPlace.save()

class UserDetail(generics.RetrieveAPIView) :
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CanPlaceList(generics.ListCreateAPIView) :
	queryset = CanPlace.objects.all()
	serializer_class = CanPlaceSerializer
	def list(self, request) :
		queryset = CanPlace.objects.filter(user = request.user).first()
		serializer = CanPlaceSerializer(queryset, context={'request': request})
		return Response(serializer.data)

class GetMap(APIView) :
	def get(self, request, format=None) :
		tiles = Tile.objects.all()
		unique_fields = ['x_coordinate', 'y_coordinate'] 
		duplicates = (tiles.values(*unique_fields)
                             .order_by()
                             .annotate(max_id=Max('id'),
                                       count_id=Count('id'))
                             .filter(count_id__gt=1))
		for duplicate in duplicates :
			for dupeTile in (tiles.filter(**{x: duplicate[x] for x in unique_fields})
                    .exclude(id=duplicate['max_id'])) :
				tiles = tiles.exclude(pk=dupeTile.pk)

		return Response({"tiles": serializers.serialize('json',tiles) })