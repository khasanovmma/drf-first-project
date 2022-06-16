from django.urls import path

from man.views import ManAPIList

urlpatterns = [
    path('manlist/', ManAPIList.as_view()),
    path('manlist/<int:pk>/', ManAPIList.as_view())
]
