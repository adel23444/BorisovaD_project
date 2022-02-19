from django.contrib import admin

from .models import (
    Otdel, Cabinet, CabinetOtdel
)
# Register your models here.
admin.site.register(Otdel)
admin.site.register(Cabinet)
admin.site.register(CabinetOtdel)