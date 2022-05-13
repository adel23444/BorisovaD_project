import json

from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q

from src.apps.documents.models import Zayavka_Polomka
from src.apps.api.serializers.documents import ZayavkaPolomkaSerializer

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Получение списка заявок",
        tags=["Заявки по поломкам"]
    )
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="Добавление заявки",
        tags=["Заявки по поломкам"]
    )
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Изменения данных заявки",
        tags=["Заявки по поломкам"]
    )
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Удаление заявки из базы",
        tags=["Заявки по поломкам"]
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Получение кабинета по ID",
        tags=["Заявки по поломкам"]
    )
)
class ZayavkaPolomkaViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    serializer_class = ZayavkaPolomkaSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Zayavka_Polomka.objects.all()

    @swagger_auto_schema(operation_summary="Получение списка заявок пользователя",
                         tags=["Заявки по поломкам"])
    @action(detail=False, methods=['get'])
    def my(self, request, *args, **kwargs):

        user = request.user
        selected = Zayavka_Polomka.objects.filter(cod_sotr=user)
        return Response(self.serializer_class(selected, many=True).data, status=status.HTTP_200_OK)