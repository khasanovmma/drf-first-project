from django.urls import path, include
from rest_framework import routers
from man.views import ManViewSet

router = routers.SimpleRouter()
router.register('man', ManViewSet)

urlpatterns = [
    path('', include(router.urls)), # http://127.0.0.1:8000/api/v1/man/
]
