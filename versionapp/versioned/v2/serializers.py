from versionapp.base import serializers as base_serializers
from versionapp.base.serializers import *


class UserSerializer(base_serializers.UserSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta(base_serializers.UserSerializer.Meta):
        fields = ('id', 'email', 'full_name','username')

    def get_full_name(self, obj):
        return '{0} {1}'.format(obj.first_name, obj.last_name)
