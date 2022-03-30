from rest_framework import serializers

from src.apps.documents.models import Zayavka_Canc

class ZayavkaCancSerializer(serializers.ModelSerializer):

    class Meta:
        model = Zayavka_Canc
        fields = '__all__'