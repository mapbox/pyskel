pyskel
======

A skeleton of a Python package with CLI and test suite included.

.. image:: https://farm4.staticflickr.com/3951/15672691531_3037819613_o_d.png

Customization quick start
-------------------------

To use pyskel as the start of a new project, do the following, preferably in
a virtual environment. Clone the repo.

.. code-block:: console

    git clone git@github.com:mapbox/pyskel.git myproject
    cd myproject

Then replace all occurrences of 'pyskel' with the name of your own project.

.. code-block:: console

    find . -not -path './.git*' -type f -exec sed -i '' -e 's/pyskel/myproject/g' {} +
    mv pyskel myproject

Then install in locally editable (``-e``) mode and run the tests.

.. code-block:: console

    pip install -e .[test]
    py.test

To try the command line script.

.. code-block:: console

    myproject --help
    myproject 4

To help prevent uncustomized forks of pyskel from being uploaded to PyPI,
I've configured the setup's upload command to dry run. Make sure to remove
this configuration from
`setup.cfg <https://docs.python.org/2/install/index.html#inst-config-syntax>`__
when you customize pyskel.

See also
--------

A post on the Mapbox blog has more information about this project:
https://www.mapbox.com/blog/pyskel/.
