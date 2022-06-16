from rest_framework import viewsets
from man.models import Man
from man.serializer import ManSerializer


class ManViewSet(viewsets.ModelViewSet):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
