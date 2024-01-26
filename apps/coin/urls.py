from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.coin.views import CoinViewSet


router = DefaultRouter()
router.register('api/coins', CoinViewSet, basename='api_coins')
urlpatterns = router.urls