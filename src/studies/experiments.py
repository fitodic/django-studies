from random import randint

from laboratory import experiment

from django.utils.functional import cached_property

from .models import ExperimentConfig


class Experiment(experiment.Experiment):
    model_class = ExperimentConfig

    def __init__(
        self,
        name,
        context=None,
        raise_on_mismatch=False,
        percent_enabled=0,
    ):
        self._experiment = self.get_experiment_config(name, percent_enabled)
        super().__init__(name, context, raise_on_mismatch)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if self._is_enabled:
            self._experiment.mark_as_ran()

        return

    def get_experiment_config(self, name, percent_enabled):
        try:
            obj = self.model_class.objects.get(name=name)
        except self.model_class.DoesNotExist:
            obj = self.model_class(name=name, percent_enabled=percent_enabled)
            obj.full_clean()
            obj.save()

        return obj

    def enabled(self):
        return self._is_enabled

    @cached_property
    def _is_enabled(self):
        """
        The cached property is here to make sure we know whether or not
        the experiment ran.

        It's a separate method/property to avoid overriding the
        `enabled` method used by the `laboratory` library as a method.

        :return: the experiment is enabled
        :rtype: bool
        """
        return (
            self._experiment.is_enabled()
            and randint(1, 100) <= self._experiment.percent_enabled
        )
