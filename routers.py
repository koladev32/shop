from rest_framework import routers

from shoe.viewsets import ShoeViewSet

router = routers.DefaultRouter()

router.register(r'shoes', ShoeViewSet)