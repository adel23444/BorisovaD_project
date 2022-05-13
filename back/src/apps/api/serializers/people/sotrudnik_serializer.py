from rest_framework import serializers

from src.apps.people.models import Sotrudnik

class SotrudnikSerializer(serializers.ModelSerializer):


    def create(self, validated_data):

        data = validated_data
        user = Sotrudnik.objects.create_user(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone=data['phone'],
            email=data['email']
        )
        user.set_password(data['password'])
        user.save()
        return user

    class Meta:
        model = Sotrudnik
        fields = ['username', 'first_name', 'last_name', 'password',
                  'email', 'phone']