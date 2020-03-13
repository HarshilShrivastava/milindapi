from retailer.api.v1.views import(
    Retailerprofile
)
from  django.urls import path

urlpatterns = [
    path('profile/',Retailerprofile.as_view()),
]