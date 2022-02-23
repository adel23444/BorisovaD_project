from django.db import models

class Sotrudnik(models.Model):

    code_sotr = models.AutoField(
        primary_key=True,
        verbose_name="Код сотрудника",
        db_column="SOTRUD_ID",
        help_text="Код сотрудника",
        unique=True
    )

    FIO = models.CharField(
        verbose_name="ФИО сотрудника",
        db_column="SOTRUD_FIO",
        help_text="ФИО сотрудника",
        max_length=255,
        null=False
    )
    #здесь возможно дополню таблицей с должностями
    dolgnost = models.CharField(
        verbose_name="Должность",
        db_column="SOTRUD_DOLG",
        help_text="Должность",
        max_length=255,
        null=True,
        blank=True
    )

    phone = models.CharField(
        verbose_name="Телефон",
        db_column="SOTRUD_PHONE",
        help_text="Телефон",
        max_length=15,
        null=True,
        blank=True
    )

    class Meta:
        db_table = "SOTRUD"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудник"