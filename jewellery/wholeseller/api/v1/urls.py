from django.urls import path,include
from wholeseller.api.v1.views import(
    wholesellerprofile,
    WholesellerOrnament,
    WholeSellerOrnamentDetail,
    add_in_bucket,
    list_of_all,
    deletefrombucket,
    add_friendM,
    list_of_sent,
    deleterequest,
    add_friendW,
    list_of_sentW,
    deleterequestW,
    ConfirmFriendrequestWRI,
    removefriendWRI
)
urlpatterns = [
    path('profile/',wholesellerprofile.as_view()),
    path('WholesellerOrnament/',WholesellerOrnament.as_view()),
    path('WholesellerOrnamentdetail/<int:pk>/',WholeSellerOrnamentDetail.as_view()),
    path('add/<int:id>',add_in_bucket),
    path('list/',list_of_all),
    path('del/<int:pk>',deletefrombucket),  
    path('add/<int:wholseller>/<int:manufacturer>/<str:message>/',add_friendM)  ,
    path('list-of-request/',list_of_sent,name="listof sent request"),
    path('delrequest/<int:id>',deleterequest,name="delete request"),
    path('addR/<int:wholseller>/<int:retailr>/<str:message>/',add_friendW)  ,
    path('list-of-requestR/',list_of_sentW,name="listof sent request"),
    path('delrequestR/<int:id>',deleterequestW,name="delete request"),
    path('confirmWRI/<int:id>/',ConfirmFriendrequestWRI),
    path('deleteWRI/<int:id>/',ConfirmFriendrequestWRI),



]