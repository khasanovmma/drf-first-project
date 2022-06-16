from django.urls import path

from man.views import ManAPIListView, ManAPIUpdateView,ManAPIDetailView

urlpatterns = [
    path('manlist/', ManAPIListView.as_view()),
    path('update/<int:pk>/', ManAPIUpdateView.as_view()),
    path('detail/<int:pk>/', ManAPIDetailView.as_view())
]
