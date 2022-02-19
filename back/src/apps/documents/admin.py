from django.contrib import admin

# Register your models here.
from .models import Zayavka_Canc, Zayavka_Polomka, Zayavka_Trans

admin.site.register(Zayavka_Canc)
admin.site.register(Zayavka_Polomka)
admin.site.register(Zayavka_Trans)