from django.urls import path
from .views import UserFormView


urlpatterns=[
    path('userfor/',UserFormView)
]