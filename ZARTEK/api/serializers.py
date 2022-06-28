from dataclasses import fields
from rest_framework import serializers
from zartekApp.models import Posts,PostImage

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'

class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['like']