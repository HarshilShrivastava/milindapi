from django.contrib import admin
from manufacturer.models import(
    Manufacturer,
    MOrnament,
    Mbucket,
    MWIR,
    MWIC
)


admin.site.register(Manufacturer)
admin.site.register(MOrnament)
admin.site.register(MWIR)
admin.site.register(Mbucket)
admin.site.register(MWIC)


