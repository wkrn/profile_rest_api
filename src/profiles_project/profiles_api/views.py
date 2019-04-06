from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """TEST API VIEW"""

    def get(self, request, format=None):
        """Return a list of APIView feature"""

        an_apiview = [
        """これはこれこれこうですが、コメントアウトしているはずです"""
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
