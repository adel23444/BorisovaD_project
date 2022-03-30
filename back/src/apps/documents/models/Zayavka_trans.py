from django.db import models

class Zayavka_Trans(models.Model):

    CREATED = 0
    ACTIVE = 1
    CLOSED = 2

    STATUS = (
        (CREATED,"Заявка создана"),
        (ACTIVE, "Заявка активна"),
        (CLOSED, "Заявка закрыта")
    )

    id = models.AutoField(
        verbose_name="Номер заявки на транспорт",
        db_column="ZAYV_TRANS_ID",
        help_text="Номер заявки на транспорт",
        primary_key=True,
        unique=True
    )
    date_zayvka = models.DateField(
        verbose_name="Дата заявки на транспорт",
        db_column="ZAYV_TRANS_DATE",
        auto_now_add=True,
        help_text="Дата заявки на транспорт",
    )
    vid_zayavka = models.IntegerField(
        verbose_name="Вид заявки",
        choices=STATUS,
        db_column="ZAYV_TRANS_VID"
    )
    date_otpr = models.DateField(
        verbose_name="Дата отправления",
        db_column="ZAYV_TRANS_DATEOTPR",
        null=True,
        blank=True,
        help_text="Дата отправления"
    )
    time_otpr = models.TimeField(
        verbose_name="Время отправления",
        db_column="ZAYV_TRANS_TIMEOTPR",
        null=True,
        blank=True,
        help_text="Время отправления"
    )

    cod_sotr = models.ForeignKey(
        to="people.Sotrudnik",
        related_name="sotrudnik_trans",
        related_query_name="sotrudnik_trans",
        verbose_name="Ссылка на сотрудника",
        on_delete=models.SET_NULL,
        db_column="ZAYV_TRANS_SOTR",
        null=True,
        blank=True,
        help_text="ID сотрудника"
    )

    killomentrs = models.IntegerField(
        verbose_name="Киллометраж",
        db_column="ZAYV_TRANS_KILLOM",
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "ZAYV_TRANS"
        verbose_name = "Заявка на транспорт"
        verbose_name_plural = "Заявка на транспорт"

