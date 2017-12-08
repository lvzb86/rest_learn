from django.contrib.auth.models import User, Group
from rest_framework import serializers


# 序列器	超链接模型序列器
class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:  # 嵌套类
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name',
                  'last_name', 'date_joined', 'groups',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'url', 'name', 'user_set',)
