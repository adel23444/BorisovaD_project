from django.db import models

class CabinetOtdel(models.Model):

    cabinet = models.ForeignKey(
        to="core.Cabinet",
        related_name="cabinet_otdel",
        related_query_name="cabinet_otdel",
        verbose_name="Ссылка на кабинет",
        on_delete=models.CASCADE,
        db_column="CABINET_ID"
    )
    otdel = models.ForeignKey(
        to="core.Otdel",
        related_name="cabinet_otdel",
        related_query_name="cabinet_otdel",
        verbose_name="Ссылка на отдел",
        on_delete=models.CASCADE,
        db_column="OTDEL_ID"
    )

    class Meta:
        db_table = "cabinet_otdel"
        verbose_name = "Связка кабинетов с отделами"
        verbose_name_plural = "Связка кабинетов с отделами"