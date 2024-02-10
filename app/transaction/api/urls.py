from rest_framework.routers import SimpleRouter

from transaction.api.views import TransactionViewSet

router = SimpleRouter()

router.register("transaction", TransactionViewSet)
urlpatterns = router.urls
