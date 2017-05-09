from django.conf.urls import url
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = router.urls