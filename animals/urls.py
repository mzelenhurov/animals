from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token

from animals import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'get_token/', obtain_jwt_token),
    path(r'', include('animals_api.urls'))
]

if settings.DEBUG:
    urlpatterns.append(path(r'docs/', include_docs_urls(title='Animals API')))
