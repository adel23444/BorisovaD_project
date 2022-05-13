from rest_framework import serializers
from django.contrib.auth.models import User
from src.apps.documents.models import Zayavka_Canc
from src.apps.api.serializers.core import TovarSerializer

class ZayavkaCancSerializer(serializers.ModelSerializer):

    tovar = TovarSerializer()
    user = serializers.CharField(read_only=True)
    users = serializers.ListField()

    def to_representation(self, instance):

        instance.user = f"{self.context['request'].user.last_name} {self.context['request'].user.first_name}"

        return super().to_representation(instance)

    class Meta:
        model = Zayavka_Canc
        fields = '__all__'