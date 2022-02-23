from django.db import models

class Tovar(models.Model):

    code_tovar = models.AutoField(
        verbose_name="Код товара",
        db_column="TOVAR_ID",
        help_text="Код товара",
        primary_key=True,
        null=False,
        unique=True
    )

    naim_tovar = models.CharField(
        verbose_name="Наименование товара",
        db_column="TOVAR_NAIM",
        help_text="Наименование товара",
        null=False,
        blank=False,
        max_length=255
    )

    kolvo_tovar = models.IntegerField(
        verbose_name="Количество товара",
        db_column="TOVAR_KOLVO",
        help_text="Количество товара",
        null=False,
        blank=False
    )

    cena_tovar = models.IntegerField(
        verbose_name="Цена за единицу",
        db_column="TOVAR_CENA",
        help_text="Цена за единицу",
        null=False,
        blank=False
    )

    class Meta:
        db_table = "TOVAR"
        verbose_name = "Товар"
        verbose_name_plural = "Товар"