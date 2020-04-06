from retailer.api.v1.views import(
    Retailerprofile,
    RetailerOrnament,
    ReatailerOrnamentDetail,
    add_in_bucket,
    deletefrombucket,
    allfrombucket,
    add_friendW,
    list_of_sentW,
    deleterequestW
)
from  django.urls import path

urlpatterns = [
    path('profile/',Retailerprofile.as_view()),
    path('ROrnament/',RetailerOrnament.as_view()),
    path('ROrnamentdetail/<int:pk>',ReatailerOrnamentDetail.as_view()),
    path('add/<int:id>/',add_in_bucket),
    path('delete/<int:pk>/',deletefrombucket),
    path('all/',allfrombucket),
    path('addR/<int:wholseller>/<int:retailr>/<str:message>/',add_friendW)  ,
    path('list-of-requestR/',list_of_sentW,name="listof sent request"),
    path('delrequestR/<int:id>',deleterequestW,name="delete request"),
]