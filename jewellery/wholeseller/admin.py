from django.contrib import admin
from wholeseller.models import(
    Wholeseller,
    WOrnament,
    WRI,
    Wbucket,
    WRIC
)
admin.site.register(Wholeseller)
admin.site.register(WOrnament)
admin.site.register(WRI)
admin.site.register(WRIC)
admin.site.register(Wbucket)
# Register your models here.
