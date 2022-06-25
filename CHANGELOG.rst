*********
Changelog
*********

The format is based on `Keep a Changelog <http://keepachangelog.com/>`_ and this project adheres to `Semantic Versioning <http://semver.org/>`_.

Changes for the upcoming release can be found in the `changelog.d` directory in this repository. Do **NOT** add changelog entries here! This changelog is managed by `towncrier <https://github.com/hawkowl/towncrier>`_ and is compiled at release time.

.. towncrier release notes start

0.1.0 (2022-06-25)
===================

Features
--------

- Integrate the ``laboratory`` library and integrate it with ``Django`` by creating a wrapper around ``laboratory.Experiment`` and a ``ExperimentConfig`` model that will allow users to adjust the percentage of impact ``percent_enabled``. ([#1](https://github.com/fitodic/django-studies/pull/1))
