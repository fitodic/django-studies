************
Contributing
************

To contribute to this project, fork it, clone it and install it in development mode:

.. code:: bash

    $ git clone git@github.com:fitodic/django-studies.git
    $ pip install -e .[dev,lint,test]

The most important dependency for development is `tox <https://tox.readthedocs.io/en/latest/>`_. It is used for running the test suite, building the documentation and changelog, validation (linting, manifest and PyPI description) and creating a new project release. To validate it is successfully installed, run:

.. code:: bash

    $ pip show tox
    Name: tox
    Version: 3.12.1
    Summary: tox is a generic virtualenv management and test command line tool
    Home-page: http://tox.readthedocs.org
    Author: Holger Krekel, Oliver Bestwalter, Bernát Gábor and others
    Author-email: None
    License: MIT
    Location: /home/username/.virtualenvs/centerline/lib/python3.7/site-packages
    Requires: py, filelock, virtualenv, setuptools, six, pluggy, toml
    Required-by:


Tests
=====

* To run the whole test suite, run:

.. code:: bash

    tox

* To display the combined coverage, run

.. code:: bash

    tox -e coverage

* To run a specific environment and display the coverage, run:

.. code:: bash

    tox -e py310-dj40-laboratory10,coverage


Changelog
=========

This project uses `towncrier <https://github.com/hawkowl/towncrier>`_ for changelog management. You don't need to install it locally since you'll be using it through ``tox``, but please adhere to the following rules:

1. For each pull request, create a new file in the `changelog.d` directory with a filename adhering to the `#pr.(feature|bugfix|doc|removal|misc).rst` schema. For example, `changelog.d/23.bugfix.rst` that is submitted in the pull request 23. ``towncrier`` will automatically add a link to the note when building the final changelog.
2. Wrap symbols like modules, functions, or classes into double backticks so they are rendered in a monospace font.
3. If you mention functions or other callables, add parentheses at the end of their names: ``func()`` or ``Class.method()``. This makes the changelog a lot more readable.

If you have any doubts, you can always render the changelog to the terminal without changing it:

.. code::

    tox -e changelog -- --draft


Releasing a new version
=======================

The CI environment should build packages and upload them to the PyPI server when a tag is pushed to `origin`. Therefore, if you want to make a new release, all you have to do is run the `release` environment in `tox`:

.. code:: bash

    $ tox -e release

This environment will merge the changelogs from the `changelog.d` directory into ``CHANGELOG.rst``, bump the **minor** version (by default) using `bumpversion <https://github.com/peritus/bumpversion>`_, commit the
changes, create a tag and push it all to `origin`.

If you want to make a **patch** release, run:

.. code::

    $ tox -e release -- patch

If Travis CI builds were successful, the new release should be automatically uploaded to `PyPI.org <https://pypi.org/>`_.
