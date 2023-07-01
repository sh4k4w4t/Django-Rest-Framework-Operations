from django.urls import path
from .views import IndiviadualUserView

urlpatterns = [
    path('api/',IndiviadualUserView.as_view())
]