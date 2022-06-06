from rest_framework import serializers

from .models import GradeItem, GradeResult


class GradeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeItem
        fields = ('date',)


class GradeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = GradeResult
        fields = '__all__'
