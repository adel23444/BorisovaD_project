from django.db import models

class Sotrudnik_Cabinet (models.Model):

    sotrudnik = models.ForeignKey(
        to="people.Sotrudnik",
        related_name="sotrudnik_cabinet",
        related_query_name="sotrudnik_cabinet",
        verbose_name="Ссылка на сотрудника",
        on_delete=models.CASCADE,
        db_column="SOTRUD_ID"
    )
    cabinet = models.ForeignKey(
        to="core.Cabinet",
        related_name="sotrudnik_cabinet",
        related_query_name="sotrudnik_cabinet",
        verbose_name="Ссылка на кабинет",
        on_delete=models.CASCADE,
        db_column="CABINET_ID"
    )


    class Meta:
        db_table = "sotrudnik_cabinet"
        verbose_name = "Связка сотрудников с кабинетами"
        verbose_name_plural = "Связка сотрудников с кабинетами"