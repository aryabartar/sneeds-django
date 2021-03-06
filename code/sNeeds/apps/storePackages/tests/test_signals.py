import json

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from rest_framework import status

from sNeeds.apps.chats.models import Chat
from sNeeds.utils.custom.TestClasses import CustomAPITestCase
from sNeeds.apps.storePackages.models import (
    StorePackage, StorePackagePhase, StorePackagePhaseThrough, SoldStorePackage,
    SoldStoreUnpaidPackagePhase, SoldStorePaidPackagePhase, ConsultantSoldStorePackageAcceptRequest,
    SoldStorePackagePhaseDetail)


class TestAPIStorePackage(CustomAPITestCase):

    def setUp(self):
        super().setUp()

        self.consultant_sold_store_package_2_accept_request_1 = ConsultantSoldStorePackageAcceptRequest.objects.create(
            sold_store_package=self.sold_store_package_2,
            consultant=self.consultant1_profile
        )

    def test_package_accept_request_deletes_after_selecting_consultant(self):
        self.assertEqual(
            ConsultantSoldStorePackageAcceptRequest.objects.filter(
                sold_store_package=self.sold_store_package_2
            ).count(),
            1
        )
        self.sold_store_package_2.consultant = self.consultant2_profile
        self.sold_store_package_2.save()

        self.assertEqual(
            ConsultantSoldStorePackageAcceptRequest.objects.filter(
                sold_store_package=self.sold_store_package_2
            ).count(),
            0
        )

    def test_package_accept_request_creates_new_chat(self):
        Chat.objects.all().delete()  # Removing previously created chats in sold time slots
        self.assertEqual(
            Chat.objects.filter(user=self.user2, consultant=self.consultant2_profile).count(),
            0
        )

        ConsultantSoldStorePackageAcceptRequest.objects.create(
            sold_store_package=self.sold_store_package_2,
            consultant=self.consultant2_profile
        )

        self.assertEqual(
            Chat.objects.filter(user=self.user2, consultant=self.consultant2_profile).count(),
            1
        )
