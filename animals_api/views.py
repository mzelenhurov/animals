from django.db.transaction import atomic
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from animals_api.models import Cat, Dog
from animals_api.permissions import IsOwner
from animals_api.serializers import CatsSerializer, DogsSerializer


class CatsViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatsSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        cats = Cat.objects.filter(owner=user)
        return cats

    @atomic
    def perform_create(self, serializer):
        super().perform_create(serializer.save(owner=self.request.user))


class DogsViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogsSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_queryset(self):
        user = self.request.user
        dogs = Dog.objects.filter(owner=user)
        return dogs

    @atomic
    def perform_create(self, serializer):
        super().perform_create(serializer.save(owner=self.request.user))
