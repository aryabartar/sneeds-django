from zeep import Client

from django.http import HttpResponse
from django.shortcuts import redirect

from rest_framework import generics, mixins, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from cart.views import *


class PublicClassPay(APIView):
    def get(self, request, *args, **kwargs):
        return Response("dd")
