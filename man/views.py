from django.forms import model_to_dict
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from man.models import Man
from man.serializer import ManSerializer


# # 1
# class ManAPIView(ListAPIView):
#     queryset = Man.objects.all()
#     serializer_class = ManSerializer

# # 2
# class ManAPIView(APIView):
#
#     def get(self, request):
#         man_list = Man.objects.all().values()
#         return Response({'posts': list(man_list)})
#
#     def post(self, request):
#         add_person = Man.objects.create(
#             full_name=request.data['full_name'],
#             content=request.data['content'],
#             category_id=request.data['category']
#         )
#         return Response({'person': model_to_dict(add_person)})

# 3
class ManAPIView(APIView):

    def get(self, request):
        man_list = Man.objects.all()
        return Response({'posts': ManSerializer(man_list, many=True).data})

    def post(self, request):
        serializer = ManSerializer(data=request.data)
        print(serializer.is_valid(raise_exception=True))
        serializer.is_valid(raise_exception=True)

        add_person = Man.objects.create(
            full_name=request.data['full_name'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'person': ManSerializer(add_person).data})
