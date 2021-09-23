from rest_framework import serializers
from main.models import short_urls

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = short_urls
        fields = "__all__"