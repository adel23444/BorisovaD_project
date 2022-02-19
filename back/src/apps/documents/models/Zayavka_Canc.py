from django.db import models

class Zayavka_Canc(models.Model):

    CREATED = 0
    ACTIVE = 1
    CLOSED = 2

    STATUS = (
        (CREATED,"Заявка создана"),
        (ACTIVE, "Заявка активна"),
        (CLOSED, "Заявка закрыта")
    )

    id = models.AutoField(
        verbose_name="Номер заявки на канцелярию",
        db_column="ZAYV_CANC_ID",
        help_text="Номер заявки на канцелярию",
        primary_key=True,
        unique=True
    )
    date_zayvka = models.DateField(
        verbose_name="Дата заявки на канцелярию",
        db_column="ZAYV_CANC_DATE",
        auto_now_add=True,
        help_text="Дата заявки на канцелярию",
    )
    vid_zayavka = models.IntegerField(
        verbose_name="Вид заявки",
        choices=STATUS,
        db_column="ZAYV_CANC_VID"
    )
   # cod_sotr = ()
   # cod_otdel = ()
   #  num_cab = ()
    summa = models.DecimalField(
        verbose_name="Общая стоимость",
        db_column="ZAYV_CANC_SUMMA",
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10
    )

    class Meta:
        db_table = "ZAYV_CANC"
        verbose_name = "Заявка на канцелярию"
        verbose_name_plural = "Заявка на канцелярию"

