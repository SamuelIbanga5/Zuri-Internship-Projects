from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from .models import Data


class DataAPIView(generics.RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class GetDataAPIView(generics.RetrieveAPIView):
    serializer_class = DataSerializer

    def get_object(self, pk):
        try:
            return Data.objects.get(pk=pk)
        except Data.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = DataSerializer(data)
        return Response(serializer.data)
