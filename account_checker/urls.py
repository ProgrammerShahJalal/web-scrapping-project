from django.urls import path
from .views import check_account_status

urlpatterns = [
    path("", check_account_status, name="check_account_status"),
]
