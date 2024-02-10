from django.urls import include, path

from transaction.apps import TransactionConfig

app_name = TransactionConfig.name


urlpatterns = [path("v1/", include("transaction.api.urls"))]
