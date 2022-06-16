from rest_framework import serializers
from rest_framework.response import Response

from man.models import Man

# 4
class ManSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Man.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.content = validated_data.get('content', instance.content)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()

        return instance