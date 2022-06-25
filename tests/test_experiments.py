import logging

import pytest

from django.urls import reverse

from studies.models import ExperimentConfig


pytestmark = [pytest.mark.django_db]


def test_view_with_matching_results(client, caplog):
    caplog.set_level(logging.INFO)

    response = client.get(reverse("matching-results"))
    assert response.status_code == 200
    assert response.json() == {"extra": "value", "result": "match"}

    assert "Experiment ViewWithMatchingResults is a match" in caplog.messages
    assert (
        ExperimentConfig.objects.get(name="ViewWithMatchingResults").last_run
        is not None
    )


def test_view_with_nonmatching_results(client, caplog):
    caplog.set_level(logging.INFO)

    response = client.get(reverse("nonmatching-results"))
    assert response.status_code == 200
    assert response.json() == {"result": "no-match", "flow": "control"}

    assert (
        "Experiment ViewWithNonMatchingResults is not a match"
        in caplog.messages
    )
    assert (
        ExperimentConfig.objects.get(
            name="ViewWithNonMatchingResults"
        ).last_run
        is not None
    )


def test_view_with_exceptional_results(client, caplog):
    caplog.set_level(logging.INFO)

    response = client.get(reverse("exceptional-results"))
    assert response.status_code == 200
    assert response.json() == {"result": "exceptional"}

    assert (
        "Experiment ViewWithExceptionalResults is not a match"
        in caplog.messages
    )
    assert (
        ExperimentConfig.objects.get(
            name="ViewWithExceptionalResults"
        ).last_run
        is not None
    )


def test_experiment_is_disabled_after_exception(client, caplog):
    caplog.set_level(logging.INFO)

    client.get(reverse("exceptional-results"))
    experiment = ExperimentConfig.objects.get(
        name="ViewWithExceptionalResults"
    )
    experiment.percent_enabled = 0
    experiment.save()
    experiment.refresh_from_db()
    assert not experiment.is_enabled()

    last_run = experiment.last_run
    client.get(reverse("exceptional-results"))
    experiment.refresh_from_db()
    assert experiment.last_run == last_run
