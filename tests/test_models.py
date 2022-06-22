import pytest

from studies.models import Experiment


pytestmark = [pytest.mark.django_db]


def test_str():
    experiment = Experiment.objects.create(name="Test", percent_enabled=10)
    assert str(experiment) == "Test (10%)"
