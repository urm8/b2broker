# Create your views here.
from django.urls import include, path

from wallet.apps import WalletConfig

app_name = WalletConfig.name

urlpatterns = [path("v1/", include("wallet.api.urls"))]
