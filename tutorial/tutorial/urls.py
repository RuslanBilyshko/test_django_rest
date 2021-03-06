# from django.conf.urls import url, include
# from django.contrib import admin
# from rest_framework import routers
#
# router = routers.DefaultRouter()
#
#
#
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api/', include('quickstart.urls')),
#     url(r'^admin/', admin.site.urls),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]