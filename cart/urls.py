from django.urls import path
from .views import Random_View


urlpatterns = [
    path('randint/', Random_View.as_view())
    ]