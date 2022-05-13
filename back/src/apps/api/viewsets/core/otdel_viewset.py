from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.apps.core.models import Otdel
from src.apps.api.serializers.core import OtdelSerializer

@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_summary="Получение списка отделов",
        tags=["Отделы"]
    )
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_summary="Добавление отдела",
        tags=["Отделы"]
    )
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_summary="Изменения данных отдела",
        tags=["Отделы"]
    )
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_summary="Удаление отдела из базы",
        tags=["Отделы"]
    )
)
@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_summary="Получение отдела по ID",
        tags=["Отделы"]
    )
)
class OtdelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch']
    serializer_class = OtdelSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Otdel.objects.all()