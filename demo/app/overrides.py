import json
import logging

from django.core.serializers.json import DjangoJSONEncoder

from studies.experiments import Experiment


logger = logging.getLogger()


class ExceptionalJSONEncoder(DjangoJSONEncoder):
    """
    An override that serializes exceptions as strings.

    We don't need anything extravagant at this point, just a simple
    output.

    """

    def default(self, o):
        try:
            return super().default(o)
        except TypeError:
            return str(o)


class ExperimentWithLogging(Experiment):
    """
    An override that provides logging support for demonstration
    purposes.

    Also useful for integration testing.

    """

    def publish(self, result):
        if result.match:
            logging.info(
                "Experiment %(name)s is a match",
                {"name": result.experiment.name},
            )
        else:
            control_observation = result.control
            candidate_observation = result.candidates[0]
            logging.info(
                json.dumps(
                    control_observation.__dict__,
                    cls=ExceptionalJSONEncoder,
                )
            )
            logging.info(
                json.dumps(
                    candidate_observation.__dict__,
                    cls=ExceptionalJSONEncoder,
                )
            )
            logging.error(
                "Experiment %(name)s is not a match",
                {"name": result.experiment.name},
            )
