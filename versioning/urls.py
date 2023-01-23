from versionapp.base.router import api_urlpatterns as api_v1
from django.urls import path,include
from versionapp.versioned.v2.router import api_urlpatterns as api_v2

urlpatterns = [
    path('api/v1/', include(api_v1)),
    path('api/v2/', include(api_v2)),
]