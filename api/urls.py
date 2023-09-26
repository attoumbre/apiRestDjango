from django.urls import path
from .views import DumpItAPI

urlpatterns = [
    path('', DumpItAPI.as_view()),
]