from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from man.models import Man, Category
from man.serializer import ManSerializer


class ManViewSet(viewsets.ModelViewSet):
    queryset = Man.objects.all()
    serializer_class = ManSerializer

    @action(methods=['get'], detail=False)
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categorY_list': [category.title for category in categories ]})
