"""
URL configuration for b2broker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
import posixpath
import re

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import finders
from django.http import Http404
from django.urls import include, path, re_path
from django.views import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="b2broker api",
        default_version="1",
    ),
    public=True,
)


def gunicorn_serve(request, path, **kwargs):
    normalized_path = posixpath.normpath(path).lstrip("/")
    absolute_path = finders.find(normalized_path)
    if not absolute_path:
        if path.endswith("/") or path == "":
            raise Http404("Directory indexes are not allowed here.")
        raise Http404("'%s' could not be found" % path)
    document_root, path = os.path.split(absolute_path)
    return static.serve(request, path, document_root=document_root, **kwargs)


urlpatterns = [
    path(
        r"swagger/",
        schema_view.with_ui("swagger", cache_timeout=0 if settings.DEBUG else 360),
        name="schema-swagger-ui",
    ),
    path("wallet/", include("wallet.urls", namespace="wallet")),
    path("transactions/", include("transaction.urls", namespace="transaction")),
    path("admin/", admin.site.urls),
    # not the best solution, but still allows gunicorn to serve static, i don't want to add any nginx or anything
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(settings.STATIC_URL.lstrip("/")), gunicorn_serve
    ),
]
