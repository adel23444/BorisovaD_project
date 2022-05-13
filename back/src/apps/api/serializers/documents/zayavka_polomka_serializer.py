from rest_framework import serializers

from src.apps.documents.models import Zayavka_Polomka

class ZayavkaPolomkaSerializer(serializers.ModelSerializer):

    type = serializers.IntegerField(read_only=True)
    status = serializers.IntegerField(read_only=True)
    user = serializers.CharField(read_only=True)

    def to_representation(self, instance):

        instance.type = 2
        instance.status = instance.vid_zayavka
        instance.user = f"{instance.cod_sotr.last_name} {instance.cod_sotr.first_name}"
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = Zayavka_Polomka
        fields = "__all__"