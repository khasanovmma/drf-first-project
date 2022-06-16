from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from man.models import Man, Category
from man.permissions import IsAdminOrReadOnly
from man.serializer import ManSerializer


class ManAPIListView(generics.ListCreateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ManAPIUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer


class ManAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Man.objects.all()
    serializer_class = ManSerializer
    permission_classes = (IsAdminOrReadOnly, )
