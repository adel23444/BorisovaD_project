from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenRefreshView, TokenObtainPairView)

from .viewsets import (CabinetViewSet, OtdelViewSet,TovarViewSet,
                        ZayavkaCancViewSet, ZayavkaPolomkaViewSet, ZayavkaTransViewSet,
                       UserInfoViewSet, SotrudnikViewSet)

app_name = "api"

router = SimpleRouter()

router.register("cabinet", CabinetViewSet, basename="cabinet")
router.register("otdel", OtdelViewSet, basename="otdel")
router.register("tovar", TovarViewSet, basename="tovar")
router.register("zayavka_canc", ZayavkaCancViewSet, basename="zayavka_canc")
router.register("zayavka_polomka", ZayavkaPolomkaViewSet, basename="zayavka_polomka")
router.register("zayavka_trans", ZayavkaTransViewSet, basename="zayavka_trans")
router.register("sotrudnik", SotrudnikViewSet, basename="sotrudnik")

urlpatterns = [
    path("token", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("user_info", UserInfoViewSet.as_view(), name="user_info")
]

urlpatterns += router.urls