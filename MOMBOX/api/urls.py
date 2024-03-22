from django.urls import path
from .views import MasterAPIView, FilteredAPIView

urlpatterns = [
  path("user/", MasterAPIView.as_view()),
  path('get_user/<int:pk>/', FilteredAPIView.as_view())
]