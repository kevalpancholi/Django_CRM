# Generated by Django 4.2.16 on 2024-12-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("earning_date", models.DateField()),
                ("cash_sale", models.DecimalField(decimal_places=2, max_digits=10)),
                ("NMS_num", models.IntegerField()),
                ("NMS_earning", models.DecimalField(decimal_places=2, max_digits=10)),
                ("flu_vacc_num", models.IntegerField()),
                ("flu_earning", models.DecimalField(decimal_places=2, max_digits=10)),
                ("covid_vacc_num", models.IntegerField()),
                ("covid_earning", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
