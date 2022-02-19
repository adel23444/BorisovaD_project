from django.db import models

class Zayavka_Polomka(models.Model):

    CREATED = 0
    ACTIVE = 1
    CLOSED = 2

    STATUS = (
        (CREATED,"Заявка создана"),
        (ACTIVE, "Заявка активна"),
        (CLOSED, "Заявка закрыта")
    )

    id = models.AutoField(
        verbose_name="Номер заявки о поломке",
        db_column="ZAYV_POLOM_ID",
        help_text="Номер заявки о поломке",
        primary_key=True,
        unique=True
    )
    date_zayvka = models.DateField(
        verbose_name="Дата заявки о поломке",
        db_column="ZAYV_POLOM_DATE",
        auto_now_add=True,
        help_text="Дата заявки о поломке",
    )
    vid_zayavka = models.IntegerField(
        verbose_name="Вид заявки",
        choices=STATUS,
        db_column="ZAYV_POLOM_VID"
    )
   # cod_sotr = ()
   # cod_otdel = ()
   #  num_cab = ()

    class Meta:
        db_table = "ZAYV_POLOMC"
        verbose_name = "Заявка о поломке"
        verbose_name_plural = "Заявка о поломке"

