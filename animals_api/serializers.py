from rest_framework import serializers
from animals_api.models import Cat, Dog


class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = "__all__"
        read_only_fields = ("owner",)


class DogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"
        read_only_fields = ("owner",)
