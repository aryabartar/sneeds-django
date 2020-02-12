from rest_framework import permissions

from sNeeds.apps.customAuth.models import ConsultantProfile


class ConsultantPermission(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """
    message = 'User should be consultant.'

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            try:
                request.user.consultant_profile
                return True
            except:
                return False


class TimeSlotSaleOwnerPermission(permissions.BasePermission):
    message = "This user is not time slot sale owner."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user

        if not user:
            return False

        if obj.consultant.user == user:
            return True

        return False


class SoldTimeSlotSaleOwnerPermission(permissions.BasePermission):
    message = "This user is not sold time slot sale owner."

    def has_object_permission(self, request, view, obj):
        user = request.user

        if user == obj.consultant.user or obj.sold_to == user:
            return True

        return False
