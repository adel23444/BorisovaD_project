from django.db import models

class Cabinet(models.Model):

    id_cabinet = models.AutoField(
        verbose_name="Код кабинета",
        db_column="CABINET_ID",
        help_text="Код кабинета",
        primary_key=True,
        unique=True
    )

    number_cabinet = models.CharField(
        verbose_name="Номер кабинета",
        db_column="CABINET_NUM",
        help_text="Номер кабинета",
        max_length=10
    )
    def __str__(self):
        return f"Кабинет №{self.number_cabinet}"
    class Meta:
        db_table = "CABINET"
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинет"