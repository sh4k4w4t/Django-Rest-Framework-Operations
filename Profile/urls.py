from django.urls import path
from .views import IndiviadualUserView, IndiviadualUserDetailsView

urlpatterns = [
    path('api/',IndiviadualUserView.as_view()),
    path('api/<int:user_id>',IndiviadualUserDetailsView.as_view())
]