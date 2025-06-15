from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class UserDeactivated(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('User is deactivated.')
    default_code = 'authentication_failed'
