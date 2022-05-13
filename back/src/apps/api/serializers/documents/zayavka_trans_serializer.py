from rest_framework import serializers

from src.apps.documents.models import Zayavka_Trans

class ZayavkaTransSerializer(serializers.ModelSerializer):

    type = serializers.IntegerField(read_only=True)
    user = serializers.CharField(read_only=True)

    def to_representation(self, instance):

        instance.type = 1
        if instance.cod_sotr:
            instance.user = f"{instance.cod_sotr.last_name} {instance.cod_sotr.first_name}"
        else:
            instance.user = ''
            instance.status = 3
        representation = super().to_representation(instance)
        return representation
    class Meta:
        model = Zayavka_Trans
        fields = "__all__"
