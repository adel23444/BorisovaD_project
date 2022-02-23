from django.db import models

class Otdel(models.Model):

    id_otdel = models.AutoField(
        verbose_name="Код отдела",
        db_column="OTDEL_ID",
        help_text="Код отдела",
        primary_key=True,
        unique=True
    )

    naim_otdel = models.CharField(
        verbose_name="Наименование отдела",
        db_column="OTDEL_NAME",
        help_text="Наименование отдела",
        null=False,
        blank=False,
        max_length=255
    )

    class Meta:
        db_table = "OTDEL"
        verbose_name = "Отдел"
        verbose_name_plural = "Отдел"