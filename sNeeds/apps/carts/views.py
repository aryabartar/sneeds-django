from rest_framework import status, generics, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from . import models


class CartListView(APIView):
    """
    POST:
    {
        "time_slot_sales" : [10,11]
    }
    """

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        data.update({"user": request.user.pk})
        serializer = serializers.CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 201)
        return Response(serializer.errors, 400)
