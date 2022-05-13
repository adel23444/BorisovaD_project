import json

from drf_yasg import openapi

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class UserInfoViewSet(views.APIView):
    my_tags = ["Информация о пользователе"]

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="Информация о пользователе",
    )
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(dir(request.user))
            return Response(
                {
                    'name': f"{request.user.last_name} {request.user.first_name}",
                    'role': request.user.username
                },
                status=status.HTTP_200_OK
            )

        else:
            return Response("Такой пользователь не найден", status=status.HTTP_400_BAD_REQUEST)