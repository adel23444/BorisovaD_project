# Generated by Django 3.2 on 2022-05-12 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0006_auto_20220512_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavka_polomka',
            name='comment',
            field=models.TextField(blank=True, db_column='ZAYV_POLOM_COMM', help_text='Комментарий', null=True, verbose_name='Комментарий'),
        ),
    ]
