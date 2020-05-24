from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.validators import ValidationError
from . import models
from .models import StudentDetailedInfo, StudentFormFieldsChoice, StudentFormApplySemesterYear

User = get_user_model()


# TODO: Move SoldTimeSlotRate

class CountrySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="account:country-detail",
        lookup_field='slug',
        read_only=True
    )

    class Meta:
        model = models.Country
        fields = ('id', 'url', 'name', 'slug', 'picture')


class UniversitySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="account:university-detail", lookup_field='slug',
                                               read_only=True)
    country = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="account:country-detail",
        lookup_field='slug',
    )

    class Meta:
        model = models.University
        fields = ('id', 'url', 'name', 'country', 'description', 'slug', 'picture')


class FieldOfStudySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="account:field-of-study-detail",
        lookup_field='slug',
        read_only=True
    )

    class Meta:
        model = models.FieldOfStudy
        fields = ('id', 'url', 'name', 'description', 'slug', 'picture')


class StudentFormFieldsChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentFormFieldsChoice
        fields = ['id', 'name', 'category', 'slug']


class StudentFormApplySemesterYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentFormApplySemesterYear
        fields = ['id', 'year', 'semester']


class StudentDetailedInfoSerializer(serializers.ModelSerializer):
    from sNeeds.apps.customAuth.serializers import SafeUserDataSerializer
    user = SafeUserDataSerializer(read_only=True)

    class Meta:
        model = StudentDetailedInfo
        fields = ['user', 'created', 'updated', 'age', 'marital_status', 'grade', 'university', 'degree_conferral_year',
                  'major', 'total_average', 'thesis_title',
                  'language_certificate', 'language_certificate_overall', 'language_speaking', 'language_listening',
                  'language_writing', 'language_reading',
                  'apply_mainland', 'apply_country', 'apply_grade', 'apply_major', 'apply_university',
                  'apply_semester_year',
                  'comment', 'resume']

        extra_kwargs = {
            'id': {'read_only': True},
            'user': {'read_only': True},
        }

    def validate(self, attrs):
        if attrs.get('grade').category != 'grade':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('grade', 'grade')))
        if attrs.get('major').category != 'major':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('major', 'major')))
        if attrs.get('university').category != 'university':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('university',
                                                                                                      'university')))
        if attrs.get('apply_grade').category != 'apply_grade':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('apply_grade',
                                                                                                      'apply_grade')))
        if attrs.get('apply_major').category != 'apply_major':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('apply_major',
                                                                                                      'apply_major')))
        if attrs.get('apply_country').category != 'apply_country':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('apply_country',
                                                                                                      'apply_country')))
        if attrs.get('apply_mainland').category != 'apply_mainland':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('apply_mainland',
                                                                                                      'apply_mainland')))
        if attrs.get('marital_status').category != 'marital_status':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('marital_status',
                                                                                                      'marital_status')))
        if attrs.get('apply_university').category != 'apply_university':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('apply_university',
                                                                                                      'apply_university')))
        if attrs.get('language_certificate').category != 'language_certificate':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('language_certificate',
                                                                                                      'language_certificate')))
        if attrs.get('degree_conferral_year').category != 'degree_conferral_year':
            raise ValidationError(_("The Value Entered for: {} is not in allowed category: {}".format('degree_conferral_year',
                                                                                                      'degree_conferral_year')))
        return attrs

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        user_student_detailed_info_qs = StudentDetailedInfo.objects.filter(user=user)
        if user_student_detailed_info_qs.exists():
            raise ValidationError(_("User already has student detailed info"))
        student_detailed_info_obj = StudentDetailedInfo.objects.create(user=user, **validated_data)
        return student_detailed_info_obj

