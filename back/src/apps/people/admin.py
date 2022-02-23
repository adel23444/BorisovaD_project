from django.contrib import admin
from .models import (
    Sotrudnik, Sotrudnik_Cabinet
)
# Register your models here.
admin.site.register(Sotrudnik)
admin.site.register(Sotrudnik_Cabinet)