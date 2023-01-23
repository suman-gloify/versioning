from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
# router.register(r'books', views.BookViewSet)

api_urlpatterns = router.urls