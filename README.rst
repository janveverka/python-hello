A Hello-World Example Python Project
====================================

This is an example of a Python project that can be packaged and shared. It's inspired by the `sample Python project <https://github.com/pypa/sampleproject>` of the `Python Packaging User Guide
<https://packaging.python.org>`_'s `Tutorial on Packaging and Distributing
Projects <https://packaging.python.org/en/latest/distributing.html>`_.

----

Commands
--------

Create a wheel:

    python setup.py bdist_wheel

Use the wheel to install his package:

    pip install <wheel-file.whl>

Run the installed file:

    hello

