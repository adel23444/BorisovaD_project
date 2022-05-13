from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.core.models import Cabinet
from src.apps.api.serializers.core import CabinetSerializer

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Получение списка кабинетов",
        tags=["Кабинеты"]
    )
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="Добавление кабинета",
        tags=["Кабинеты"]
    )
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Изменения данных кабинета",
        tags=["Кабинеты"]
    )
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Удаление кабинета из базы",
        tags=["Кабинеты"]
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Получение кабинета по ID",
        tags=["Кабинеты"]
    )
)
class CabinetViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    serializer_class = CabinetSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Cabinet.objects.all()