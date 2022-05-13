from django.db import models

class Zayavka_Polomka(models.Model):

    ACTIVE = 0
    CLOSED = 1

    STATUS = (
        (ACTIVE, "Активная"),
        (CLOSED, "Завершена")
    )

    id = models.AutoField(
        verbose_name="Номер заявки о поломке",
        db_column="ZAYV_POLOM_ID",
        help_text="Номер заявки о поломке",
        primary_key=True,
        unique=True
    )

    date_zayavka = models.DateField(
        verbose_name="Дата заявки о поломке",
        db_column="ZAYV_POLOM_DATE",
        auto_now_add=True,
        help_text="Дата заявки о поломке",
    )

    vid_zayavka = models.IntegerField(
        verbose_name="Статус заявки",
        choices=STATUS,
        db_column="ZAYV_POLOM_VID"
    )

    cod_sotr = models.ForeignKey(
        to="people.Sotrudnik",
        related_name="sotrudnik_pol",
        related_query_name="sotrudnik_pol",
        verbose_name="Ссылка на сотрудника",
        on_delete=models.SET_NULL,
        db_column="ZAYV_POLOM_SOTR",
        null=True,
        blank=True,
        help_text="ID сотрудника"
    )

    comment = models.TextField(
        verbose_name="Комментарий",
        db_column="ZAYV_POLOM_COMM",
        help_text="Комментарий",
        null=True,
        blank=True
    )
    class Meta:
        db_table = "ZAYV_POLOMC"
        verbose_name = "Заявка о поломке"
        verbose_name_plural = "Заявка о поломке"

