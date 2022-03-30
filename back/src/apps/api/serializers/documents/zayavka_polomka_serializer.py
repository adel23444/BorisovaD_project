from rest_framework import serializers

from src.apps.documents.models import Zayavka_Polomka

class ZayavkaPolomkaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zayavka_Polomka
        fields = "__all__"