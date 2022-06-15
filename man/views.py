from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from man.models import Man
from man.serializer import ManSerializer

#
# class ManAPIView(ListAPIView):
#     queryset = Man.objects.all()
#     serializer_class = ManSerializer


class ManAPIView(APIView):
    def get(self, request):
        return Response({'full_name': 'Jackie Chan'})
