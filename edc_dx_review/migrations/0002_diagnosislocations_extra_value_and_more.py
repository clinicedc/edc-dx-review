# Generated by Django 4.2.3 on 2023-08-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_dx_review", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diagnosislocations",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="historicaldiagnosislocations",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="historicalreasonsfortesting",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name="reasonsfortesting",
            name="extra_value",
            field=models.CharField(max_length=250, null=True),
        ),
    ]