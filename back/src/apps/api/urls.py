from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .viewsets import CabinetViewSet, OtdelViewSet

app_name = "api"

router = SimpleRouter()

router.register("cabinet", CabinetViewSet, basename="cabinet")
router.register("otdel", OtdelViewSet, basename="otdel")

urlpatterns = [
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns += router.urls