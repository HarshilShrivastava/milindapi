from manufacturer.api.v1.views import (
    Manufacturerprofile,
    ManufacturerOrnament,
    ManufacturerOrnamentDetail,
    add_in_bucket,
    list_of_all,
    deletefrombucket,
    add,
    list_of_sent,
    deleterequest,
    ConfirmFriendrequestMWI,
    removefriendMWI

)
from  django.urls import path

urlpatterns = [
    path('profile/',Manufacturerprofile.as_view()),
    path('ManufactureOrnament/',ManufacturerOrnament.as_view()),
    path('ManufactureOrnament1/<int:pk>/',ManufacturerOrnamentDetail.as_view()),
    path('add/<int:id>/',add_in_bucket),
    path('list/',list_of_all),
    path('del/<int:pk>/',deletefrombucket),
    path('add/<int:wholseller>/<int:manufacturer>/<str:message>/',add)  ,
    path('list-of-request/',list_of_sent,name="listof sent request"),
    path('delrequest/<int:id>/',deleterequest,name="delete request"),
    path('confirm-request/<int:id>/',ConfirmFriendrequestMWI),
    path('remove-friend/<int:id>/',removefriendMWI),

]