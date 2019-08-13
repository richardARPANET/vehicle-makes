**NOTICE**: If you're reading this on GitHub.com please be aware this is a mirror of the primary remote located at https://code.richard.do/richardARPANET/vehicle-makes.
Please direct issues and pull requests there.

vehicle-makes
=======

|PyPI| |Python Versions| |Build Status|

Python library to provide up-to-date vehicle make and model data. Currently returning cars only. The data source is AutoTrader.

Installation
------------

To install, simply:

.. code:: bash

    pip install vehicle-makes

How to use
------------


.. code:: python

    from vehicle_makes import get_makes_and_models

    makes_and_models = get_makes_and_models()


``get_makes_and_models()`` returns a dict in the following structure:


.. code:: python

    {
        'AC': ('212', '302', 'Cobra'),
        'Abarth': ('124 Spider', '500', '500C', '595',),
    }


Requirements
------------

::

    1. Python 3.6+
    2. See requirements.txt

Running the tests
-----------------

.. code:: bash

    pip install -r requirements-dev.txt
    pytest src/tests/tests.py

.. |PyPI| image:: https://img.shields.io/pypi/v/vehicle-makes.svg
   :target: https://pypi.python.org/pypi/vehicle-makes
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/vehicle-makes.svg
   :target: https://pypi.python.org/pypi/vehicle-makes
.. |Build Status| image:: https://travis-ci.org/richardARPANET/vehicle-makes.png?branch=master
   :target: https://travis-ci.org/richardARPANET/vehicle-makes
