from rest_framework import serializers
from django.contrib.auth.models import User
from rPlaceApp.models import Tile, CanPlace

class TileSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.HyperlinkedIdentityField(view_name = 'user-detail', read_only=True)
	class Meta:
		model = Tile
		fields = ('date_time_created', 'x_coordinate', 'y_coordinate', 'colour', 'owner',)

class UserSerializer(serializers.HyperlinkedModelSerializer) :
	tiles = serializers.HyperlinkedIdentityField(many = True, view_name = 'tile-detail', read_only=True)
	# canplace = serializers.HyperlinkedIdentityField(many = False, view_name = 'canplace', read_only=True)

	class Meta:
		model = User
		fields = ('url', 'id', 'username', 'tiles',)

class CanPlaceSerializer(serializers.HyperlinkedModelSerializer) :
	user = serializers.HyperlinkedIdentityField(view_name = 'user-detail', read_only=True)
	class Meta :
		model = CanPlace
		fields = ('user', 'time_to_place',)