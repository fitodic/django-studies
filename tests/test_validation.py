import pytest

from django.core.exceptions import ValidationError

from studies.models import Experiment
from studies.proxies import ExperimentProxy


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize("percent_enabled", [0, 10, 50, 90, 100])
def test_experiments_are_created_with_valid_percentages(percent_enabled):
    name = "Valid percentage"
    ExperimentProxy(name, percent_enabled=percent_enabled)
    experiment = Experiment.objects.get(name=name)
    assert experiment.percent_enabled == percent_enabled


@pytest.mark.parametrize("percent_enabled", [-10, 110])
def test_experiments_are_created_with_invalid_percentages(percent_enabled):
    with pytest.raises(ValidationError):
        ExperimentProxy("Invalid percentage", percent_enabled=percent_enabled)

    assert Experiment.objects.count() == 0
