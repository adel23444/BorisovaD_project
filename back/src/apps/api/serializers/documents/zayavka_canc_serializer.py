from rest_framework import serializers
from src.apps.documents.models import Zayavka_Canc
from src.apps.api.serializers.core import TovarSerializer

class ZayavkaCancSerializer(serializers.ModelSerializer):

    tovar_name = serializers.CharField(read_only=True)
    tovar_kolvo = serializers.IntegerField(read_only=True)
    tovar_cena = serializers.IntegerField(read_only=True)
    type = serializers.IntegerField(read_only=True)
    user = serializers.CharField(read_only=True)
    tovar = TovarSerializer()
    def to_representation(self, instance):

        instance.type = 0
        if instance.ispolnitel:
            instance.user = f"{instance.ispolnitel.last_name} {instance.ispolnitel.first_name}"
        else:
            instance.user = ''
            instance.status = 3
        instance.tovar_name = instance.tovar.naim_tovar
        instance.tovar_kolvo = instance.tovar.kolvo_tovar
        instance.tovar_cena = instance.tovar.cena_tovar
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = Zayavka_Canc
        fields = '__all__'