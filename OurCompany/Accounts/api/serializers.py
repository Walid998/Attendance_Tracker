from rest_framework import serializers
from Accounts.models import UsersLogs
from django.contrib.auth.models import User

class UsersLogsSerializer(serializers.ModelSerializer):
    user_id = serializers.RelatedField(source='User', read_only=True)

    class Meta:
        model = UsersLogs
        fields = ['user_id', 'logedin_at', 'leave_request_at', 'logedout_at', 'is_logedout']