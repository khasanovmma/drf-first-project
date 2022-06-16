from rest_framework import serializers
from rest_framework.response import Response

from man.models import Man


# 4
class ManSerializer(serializers.ModelSerializer):
    class Meta:
        model = Man
        fields = '__all__'
