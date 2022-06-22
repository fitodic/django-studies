from django.http import JsonResponse
from django.views.generic import View

from .overrides import ExperimentWithLogging


class ViewWithMatchingResults(View):
    def get(self, request, *args, **kwargs):
        with ExperimentWithLogging(
            name="ViewWithMatchingResults",
            context={"context_key": "context_value"},
            percent_enabled=100,
        ) as experiment:
            arg = "match"
            kwargs = {"extra": "value"}
            experiment.control(
                self._get_control,
                context={"strategy": "control"},
                args=[arg],
                kwargs=kwargs,
            )
            experiment.candidate(
                self._get_candidate,
                context={"strategy": "candidate"},
                args=[arg],
                kwargs=kwargs,
            )
            data = experiment.conduct()

        return JsonResponse(data)

    def _get_control(self, result, **kwargs):
        return {"result": result, **kwargs}

    def _get_candidate(self, result, **kwargs):
        return {"result": result, **kwargs}


class ViewWithNonMatchingResults(View):
    def get(self, request, *args, **kwargs):
        with ExperimentWithLogging(
            name="ViewWithNonMatchingResults",
            context={"context_key": "context_value"},
            percent_enabled=100,
        ) as experiment:
            arg = "no-match"
            experiment.control(
                self._get_control, context={"strategy": "control"}, args=[arg]
            )
            experiment.candidate(
                self._get_candidate,
                context={"strategy": "candidate"},
                args=[arg],
            )
            data = experiment.conduct()

        return JsonResponse(data)

    def _get_control(self, result):
        return {"result": result, "flow": "control"}

    def _get_candidate(self, result):
        return {"result": result, "flow": "candidate"}


class ViewWithExceptionalResults(View):
    def get(self, request, *args, **kwargs):
        with ExperimentWithLogging(
            name="ViewWithExceptionalResults",
            context={"context_key": "context_value"},
            percent_enabled=100,
        ) as experiment:
            arg = "exceptional"
            experiment.control(
                self._get_control, context={"strategy": "control"}, args=[arg]
            )
            experiment.candidate(
                self._get_candidate,
                context={"strategy": "candidate"},
                args=[arg],
            )
            data = experiment.conduct()

        return JsonResponse(data)

    def _get_control(self, result):
        return {"result": result}

    def _get_candidate(self, result):
        raise Exception("Candidate call failed")
