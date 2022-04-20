from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from shoe.models import Shoe
from shoe.serializers import ShoeSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['get'] 