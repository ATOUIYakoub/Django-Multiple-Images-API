from rest_framework import generics
from .models import Image
from .serializers import ImageSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ImageView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @swagger_auto_schema(operation_summary='Create a new image',
                         request_body=openapi.Schema(
                             type=openapi.TYPE_OBJECT,
                             required=['title', 'description'],
                             properties={
                                 'title': openapi.Schema(type=openapi.TYPE_STRING),
                                 'description': openapi.Schema(type=openapi.TYPE_STRING),
                                 'images': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'image': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY)}))
                             },
                         ),
                         responses={201: 'Created'})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

