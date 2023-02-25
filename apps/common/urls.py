from django.urls import path
from .views import CurrentDateView, IndexView, TextView


urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('hello/', TextView.as_view()),
]
