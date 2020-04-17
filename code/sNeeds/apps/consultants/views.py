from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, filters, pagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from sNeeds.apps.consultants.models import ConsultantProfile
from sNeeds.apps.consultants.serializers import ConsultantProfileSerializer
from .filters import ConsultantProfileFilter
from .paginators import StandardResultsSetPagination


class ConsultantProfileDetail(APIView):
    def get_object(self, slug):
        try:
            return ConsultantProfile.objects.get(slug=slug)
        except ConsultantProfile.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        consultant_profile = self.get_object(slug)
        serializer = ConsultantProfileSerializer(
            consultant_profile,
            context={"request": request}
        )
        return Response(serializer.data)


class ConsultantProfileList(generics.ListAPIView):
    serializer_class = ConsultantProfileSerializer
    ordering_fields = ['rate', 'created', ]

    # TODO: After Deploy
    # uncomment filterset_class and delete filterset_fields to use custom filter class (ConsultantProfileFilter)
    filterset_fields = ['universities', 'field_of_studies', 'countries', 'active', ]

    # filterset_class = ConsultantProfileFilter

    def get_queryset(self):
        return ConsultantProfile.objects.filter(active=True).at_least_one_time_slot()


class ConsultantProfileListTemp(ConsultantProfileList):
    pagination_class = StandardResultsSetPagination
