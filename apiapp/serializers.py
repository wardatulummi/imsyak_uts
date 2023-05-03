from rest_framework import serializers
from .models import jadwal

class jadwalSerializer(serializers.ModelSerializer):
    class Meta:
        model = jadwal
        fields = "__all__"