from rest_framework import serializers
from .models import Mini


class MiniSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mini
        fields=[
            'name',
            'title',
            'date',
        ]