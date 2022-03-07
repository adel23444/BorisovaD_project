from django.db import models
from src.apps.people.models import Sotrudnik
class Zayavka_Canc(models.Model):

    ACTIVE = 0
    CLOSED = 1

    STATUS = (
        (ACTIVE, "Активная"),
        (CLOSED, "Завершена")
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

    zayavitel = models.ForeignKey(
        to="people.Sotrudnik",
        related_name="zayavitel",
        related_query_name="zayavitel",
        verbose_name="Заявитель",
        on_delete=models.CASCADE,
        db_column="ZAYV_CANC_ZAYAVITEL",
        null=True
    )

    ispolnitel = models.ForeignKey(
        to="people.Sotrudnik",
        related_name="ispolnitel",
        related_query_name="ispolnitel",
        verbose_name="Исполнитель",
        on_delete=models.CASCADE,
        db_column="ZAYV_CANC_ISPOLNITEL",
        null=True
    )

    tovar = models.ForeignKey(
        to="core.Tovar",
        related_name="tovar",
        related_query_name="tovar",
        verbose_name="Товар",
        on_delete=models.CASCADE,
        db_column="ZAYV_CANC_TOVAR"
    )

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

