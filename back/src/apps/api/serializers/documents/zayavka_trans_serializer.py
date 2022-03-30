from rest_framework import serializers

from src.apps.documents.models import Zayavka_Trans

class ZayavkaTransSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zayavka_Trans
        fields = "__all__"
