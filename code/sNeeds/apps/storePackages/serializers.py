from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import StorePackagePhase, StorePackagePhaseThrough, StorePackage, ConsultantSoldStorePackageAcceptRequest
from ..consultants.models import ConsultantProfile
from ..customAuth.serializers import SafeUserDataSerializer


class StorePackagePhaseThroughSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        view_name='store-package:store-package-phase-through-detail',
    )
    store_package = serializers.HyperlinkedRelatedField(
        lookup_field='slug',
        read_only=True,
        view_name='store-package:store-package-detail'
    )
    title = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    class Meta:
        model = StorePackagePhaseThrough
        fields = ['id', 'url', 'title', 'store_package', 'phase_number', 'price']

    def get_title(self, obj):
        return obj.store_package_phase.title

    def get_price(self, obj):
        return obj.store_package_phase.price


class StorePackageSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        lookup_field='slug',
        view_name='store-package:store-package-detail',
    )

    store_package_phases = serializers.HyperlinkedRelatedField(
        lookup_field='id',
        many=True,
        read_only=True,
        view_name='store-package:store-package-phase-through-detail'
    )

    class Meta:
        model = StorePackage
        fields = ["id", 'url', "price", "total_price", "active", "title", "store_package_phases", ]


class ConsultantSoldStorePackageAcceptRequestSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        lookup_field='id',
        view_name='store-package:consultant-sold-store-package-accept-request-detail'
    )

    class Meta:
        model = ConsultantSoldStorePackageAcceptRequest
        fields = ['id', 'url', 'sold_store_package', 'consultant', 'created', 'updated']


class SoldStorePackageSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     lookup_field='id',
    #     view_name='store-package:consultant-sold-store-package-accept-request-detail'
    # )
    sold_to = serializers.SerializerMethodField()
    consultant_url = serializers.HyperlinkedRelatedField(
        source='consultant',
        lookup_field='slug',
        read_only=True,
        view_name='consultant:consultant-profile-detail'
    )

    class Meta:
        model = ConsultantSoldStorePackageAcceptRequest
        fields = ['title', 'sold_to', 'consultant', 'paid_price', 'total_price', 'created', 'updated']

    def get_sold_to(self, obj):
        return SafeUserDataSerializer(obj.sold_to).data
