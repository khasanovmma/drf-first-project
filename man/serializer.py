from rest_framework import serializers
from rest_framework.response import Response

from man.models import Man


# 4
class ManSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Man
        fields = '__all__'
