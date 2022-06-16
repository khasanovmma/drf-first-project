from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from man.models import Man
from man.serializer import ManSerializer

# 4
class ManAPIView(APIView):
    def get(self, request):
        man_list = Man.objects.all()
        return Response({'person_list': ManSerializer(man_list, many=True).data})

    def post(self, request):
        serializer = ManSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'person': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Man.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})

        serializer = ManSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'person_data_updated': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        try:
            person = Man.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not allowed'})
        person.delete()


        return Response({'person_delete': f'Delete person {pk}'})
