from django.db import models
from django.contrib.auth.models import AbstractUser

class Sotrudnik(AbstractUser):

    id = models.AutoField(
        primary_key=True,
        verbose_name="Код сотрудника",
        db_column="SOTRUD_ID",
        help_text="Код сотрудника",
        unique=True
    )

    username = models.CharField(
        verbose_name="Имя профиля",
        db_column="SOTRUD_FIO",
        help_text="Имя профиля",
        max_length=255,
        unique=True,
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

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        db_table = "SOTRUD"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудник"