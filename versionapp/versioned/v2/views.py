from versionapp.base.views import *
from versionapp.base import views as base_views
from . import serializers as v2_serializers


class UserViewSet(base_views.UserViewSet):
    serializer_class = v2_serializers.UserSerializer