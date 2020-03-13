from manufacturer.api.v1.views import (
    Manufacturerprofile
)
from  django.urls import path

urlpatterns = [
    path('profile/',Manufacturerprofile.as_view()),
]