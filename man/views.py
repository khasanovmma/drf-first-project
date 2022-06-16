from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from man.models import Man
from man.serializer import ManSerializer


class ManAPIList(generics.ListCreateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
