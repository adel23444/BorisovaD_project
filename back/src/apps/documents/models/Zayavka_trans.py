from django.db import models

class Zayavka_Trans(models.Model):
    ACTIVE = 1
    CLOSED = 2

    STATUS = (
        (ACTIVE, "Активная"),
        (CLOSED, "Завершена")
    )

    id = models.AutoField(
        verbose_name="Номер заявки на транспорт",
        db_column="ZAYV_TRANS_ID",
        help_text="Номер заявки на транспорт",
        primary_key=True,
        unique=True
    )
    date_zayavka = models.DateField(
        verbose_name="Дата заявки на транспорт",
        db_column="ZAYV_TRANS_DATE",
        auto_now_add=True,
        help_text="Дата заявки на транспорт",
    )
    status = models.IntegerField(
        verbose_name="Статус",
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

    punkt_nazn = models.CharField(
        verbose_name="Пункт назначения",
        db_column="ZAYV_TRANS_PUNKT",
        help_text="Пункт назначения",
        max_length=255,
        null=True,
        blank=True
    )

    address = models.CharField(
        verbose_name="Адрес",
        db_column="ZAYV_TRANS_ADRES",
        help_text="Адрес",
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "ZAYV_TRANS"
        verbose_name = "Заявка на транспорт"
        verbose_name_plural = "Заявка на транспорт"

