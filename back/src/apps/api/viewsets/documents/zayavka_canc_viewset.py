from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

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
    queryset = Zayavka_Canc.objects.all()