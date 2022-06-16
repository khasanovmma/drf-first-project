from django.urls import path, include
from rest_framework import routers
from man.views import ManAPIListView, ManAPIUpdateView, ManAPIDestroyView


urlpatterns = [
    path('man/', ManAPIListView.as_view()),
    path('man/<int:pk>/', ManAPIUpdateView.as_view()),
    path('man-delete/<int:pk>/', ManAPIDestroyView.as_view()),
]
