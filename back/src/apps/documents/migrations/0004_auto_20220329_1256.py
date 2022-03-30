# Generated by Django 3.2 on 2022-03-29 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('documents', '0003_auto_20220307_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='zayavka_polomka',
            name='cod_sotr',
            field=models.ForeignKey(blank=True, db_column='ZAYV_POLOM_SOTR', help_text='ID сотрудника', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sotrudnik_pol', related_query_name='sotrudnik_pol', to='people.sotrudnik', verbose_name='Ссылка на сотрудника'),
        ),
        migrations.AddField(
            model_name='zayavka_trans',
            name='cod_sotr',
            field=models.ForeignKey(blank=True, db_column='ZAYV_TRANS_SOTR', help_text='ID сотрудника', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sotrudnik_trans', related_query_name='sotrudnik_trans', to='people.sotrudnik', verbose_name='Ссылка на сотрудника'),
        ),
    ]