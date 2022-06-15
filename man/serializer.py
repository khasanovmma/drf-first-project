from rest_framework.serializers import ModelSerializer

from man.models import Man


class ManSerializer(ModelSerializer):
    class Meta:
        model = Man
        fields = ('full_name', 'category')
