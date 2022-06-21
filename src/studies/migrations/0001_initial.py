# Generated by Django 4.0.5 on 2022-06-21 16:20

from django.db import migrations, models
import studies.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Experiment",
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
                (
                    "name",
                    models.CharField(
                        editable=False,
                        help_text="The trial's name set by the system.",
                        max_length=100,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "percent_enabled",
                    models.SmallIntegerField(
                        default=0,
                        help_text="Set it to 0 (zero) if you want to disable the trial.",
                        validators=[studies.validators.validate_percent],
                        verbose_name="Percent of users that will be impacted by this trial",
                    ),
                ),
            ],
            options={
                "verbose_name": "Experiment",
                "verbose_name_plural": "Experiments",
                "ordering": ["name"],
            },
        ),
    ]
