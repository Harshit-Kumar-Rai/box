from django.urls import path
from .views import MasterAPIView

urlpatterns = [
  path("user/", MasterAPIView.as_view())
]