from rest_framework import serializers
from .models import Image, ImageFile

class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = ['image']

class ImageSerializer(serializers.ModelSerializer):
    images = ImageFileSerializer(many=True)

    class Meta:
        model = Image
        fields = '__all__'
