from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.generics import GenericAPIView
from rest_framework.exceptions import NotFound

from tg.models import Announce
from . import services
from .serializers import AnnounceSerializer


class AnnounceView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = AnnounceSerializer

    def get_object(self, *args, **kwargs):
        try:
            product = Announce.objects.get(user_id=kwargs['id'])
        except Exception as e:
            raise NotFound('not found product')
        return product

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        root = serializer.save()
        result = services.one_product(request, root.id)
        print(result)
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        root = self.get_object(*args, **kwargs)
        serializer = self.get_serializer(data=request.data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        print("data8787878787878", data)
        result = services.one_product(request, data.id)
        return Response(result, status=status.HTTP_200_OK, content_type='application/json')

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs and kwargs['id']:
            result = services.one_product(request, id=kwargs['id'])
        else:
            result = {"item": None}
        return Response(result, status=status.HTTP_200_OK, content_type='application/json')
