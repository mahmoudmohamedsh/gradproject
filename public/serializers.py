from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    created_at = serializers.ImageField(read_only=True)
    class Meta:
        model = Announcement
        fields = ('title','img','created_at')