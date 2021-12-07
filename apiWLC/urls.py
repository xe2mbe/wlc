from django.urls import include, path

from rest_framework import routers

from apiWLC.views import GuestUserViewSet, APViewSet

router = routers.DefaultRouter()
router.register(r'guestuser', GuestUserViewSet)
router.register(r'ap', APViewSet)

urlpatterns = [
   path('', include(router.urls)),
]