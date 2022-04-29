from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

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
    queryset = Zayavka_Polomka.objects.all()