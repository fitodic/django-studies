from random import randint

from laboratory import experiment

from . import models


class Experiment(experiment.Experiment):
    model_class = models.Experiment

    def __init__(
        self,
        name,
        context=None,
        raise_on_mismatch=False,
        percent_enabled=0,
    ):
        self._experiment = self.get_experiment_config(name, percent_enabled)
        super().__init__(name, context, raise_on_mismatch)

    def get_experiment_config(self, name, percent_enabled):
        return self.model_class.objects.get_or_create(
            name=name, defaults={"percent_enabled": percent_enabled}
        )

    def enabled(self):
        return (
            self._experiment.is_enabled
            and randint(1, 100) < self.percent_enabled
        )
