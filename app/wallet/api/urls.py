from rest_framework.routers import SimpleRouter

from wallet.api.views import WalletViewSet

router = SimpleRouter()

router.register("wallet", WalletViewSet)
urlpatterns = router.urls
