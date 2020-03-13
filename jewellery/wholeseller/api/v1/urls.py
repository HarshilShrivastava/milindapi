from django.urls import path,include
from wholeseller.api.v1.views import(
    wholesellerprofile
)
urlpatterns = [
    path('profile/',wholesellerprofile.as_view()),
]