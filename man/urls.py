from django.urls import path

from man.views import ManAPIView

urlpatterns = [
    path('manlist/', ManAPIView.as_view())
]
