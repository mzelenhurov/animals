from django.urls import path, include
from rest_framework import routers
from animals_api.views import CatsViewSet, DogsViewSet

router = routers.DefaultRouter()
router.register(r"cats", CatsViewSet, basename="cats"),
router.register(r"dogs", DogsViewSet, basename="dogs")

urlpatterns = [
    path(r'', include(router.urls))
]