from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from src.apps.documents.models import Zayavka_Canc
from src.apps.api.serializers.documents import ZayavkaCancSerializer

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Получение списка заявок",
        tags=["Заявки по канц. товарам"]
    )
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="Добавление заявки",
        tags=["Заявки по канц. товарам"]
    )
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Изменения данных заявки",
        tags=["Заявки по канц. товарам"]
    )
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Удаление заявки из базы",
        tags=["Заявки по канц. товарам"]
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Получение заявки по ID",
        tags=["Заявки по канц. товарам"]
    )
)
class ZayavkaCancViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    serializer_class = ZayavkaCancSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Zayavka_Canc.objects.all()

    @swagger_auto_schema(operation_summary="Получение списка заявок пользователя",
                         tags=["Заявки по канц. товарам"])
    @action(detail=False, methods=['get'])
    def my(self, request, *args, **kwargs):
        user = request.user
        selected = Zayavka_Canc.objects.filter(ispolnitel=user)
        return Response(self.serializer_class(selected, many=True).data, status=status.HTTP_200_OK)