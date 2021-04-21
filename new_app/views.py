from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class pingRespose(APIView):
    authentication_classes = ()
    permission_classes = []

    def get(self, request, format=None):
        """
        Return users details.
        """
        data = {"message": "pong"}
        return Response(data, status = status.HTTP_200_OK)