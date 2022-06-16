import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from man.models import Man
# # 1
# class ManSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Man
#         fields = ('full_name', 'category')

# # 3
# class ManModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content




# # # 3
# class ManSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()

# # 3
class ManSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

# # 3
# def encode():
#     model = ManModel('Denzel Washington',
#                      'Content: American actor celebrated for his engaging and powerful performances.')
#     model_sr = ManSerializer(model)
#     print(model_sr.data, type(model_sr.data))
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Denzel Washington","content":"Content: American actor celebrated for his engaging and powerful performances."}')
#     data = JSONParser().parse(stream)
#     serializer = ManSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)