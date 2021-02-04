from rest_framework import serializers
from .models import Movie
from django.contrib.auth.models import AbstractUser


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('id', 'created_date', 'updated_date',)