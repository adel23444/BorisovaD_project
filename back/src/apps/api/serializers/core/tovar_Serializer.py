from rest_framework import serializers

from src.apps.core.models import Tovar

class TovarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tovar
        fields = "__all__"