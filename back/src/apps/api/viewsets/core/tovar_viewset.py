from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from src.apps.core.models import Tovar
from src.apps.api.serializers.core import TovarSerializer

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Получение списка товаров",
        tags=["Товары"]
    )
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="Добавление товара",
        tags=["Товары"]
    )
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Изменения данных товара",
        tags=["Товары"]
    )
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Удаление товара из базы",
        tags=["Товары"]
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Получение товара по ID",
        tags=["Товары"]
    )
)
class TovarViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    serializer_class = TovarSerializer
    queryset = Tovar.objects.all()