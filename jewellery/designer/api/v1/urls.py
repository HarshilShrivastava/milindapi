from designer.api.v1.views import(
    Designerrprofile
)

from  django.urls import path

urlpatterns = [
    path('profile/',Designerrprofile.as_view()),
]