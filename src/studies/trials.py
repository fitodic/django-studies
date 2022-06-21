from random import randint

from laboratory import experiment

from . import models


class ExperimentProxy(experiment.Experiment):
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
        try:
            obj = self.model_class.objects.get(name=name)
        except self.model_class.DoesNotExist:
            obj = self.model_class(name=name, percent_enabled=percent_enabled)
            obj.full_clean()
            obj.save()

        return obj

    def enabled(self):
        return (
            self._experiment.is_enabled
            and randint(1, 100) < self.percent_enabled
        )
