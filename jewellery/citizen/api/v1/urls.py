from citizen.api.v1.views import (
    Citizenprofile
)
from  django.urls import path

urlpatterns = [
    path('profile/',Citizenprofile.as_view()),
]