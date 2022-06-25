from django.contrib import admin
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from .validators import validate_percent


class ExperimentConfig(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        unique=True,
        editable=False,
        help_text=_("The experiment's name set by the system."),
    )
    percent_enabled = models.SmallIntegerField(
        _("Percent of users that will be impacted"),
        validators=[validate_percent],
        default=0,
        help_text=_(
            "Set it to 0 (zero) if you want to disable the experiment."
        ),
    )
    first_run = models.DateTimeField(_("First run"), auto_now_add=True)
    last_run = models.DateTimeField(
        _("Last run"),
        null=True,
        default=None,
        editable=False,
    )

    class Meta:
        verbose_name = _("Experiment config")
        verbose_name_plural = _("Experiment configs")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.percent_enabled}%)"

    @admin.display(boolean=True)
    def is_enabled(self):
        return self.percent_enabled > 0

    def mark_as_ran(self):
        self.last_run = now()
        self.save(update_fields=["last_run"])
