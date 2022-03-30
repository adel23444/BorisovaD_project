from rest_framework import serializers

from src.apps.core.models import Otdel

class OtdelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Otdel
        fields = '__all__'