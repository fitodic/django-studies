from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_percent


class Experiment(models.Model):
    name = models.CharField(
        _("Name"),
        max_length=100,
        unique=True,
        editable=False,
        help_text=_("The trial's name set by the system."),
    )
    percent_enabled = models.SmallIntegerField(
        _("Percent of users that will be impacted by this trial"),
        validators=[validate_percent],
        default=0,
        help_text=_("Set it to 0 (zero) if you want to disable the trial."),
    )

    class Meta:
        verbose_name = _("Experiment")
        verbose_name_plural = _("Experiments")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.percent_enabled}%)"

    @property
    def is_enabled(self):
        return self.percent_enabled > 0
