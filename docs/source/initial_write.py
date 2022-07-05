import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../project'))
from load_config import instance
from modules import file_write
import get_names

index_file_name = 'index.rst'
index = f"""
Welcome to {instance.project_name.title()}
===================================

{instance.desc}

Check out the :doc:`usage` section for further information, including how to
:ref:`install <installation>` the project.

Contents
--------

.. toctree::

   usage
"""

for file_name in get_names.file_names:
    index += "   " + file_name[:-4] + "\n"

usage_file_name = 'usage.rst'
usage = f"""
Usage
=====

.. _installation:

Installation
------------

To use {instance.project_name.title()}, first install it using `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: console

   (.venv) $ pip install {instance.project_name}
"""

active = """
.. note::

   This project is under active development.
"""

if instance.active:
    index += active

file_write.write(index_file_name, 'a', index)
file_write.write(usage_file_name, 'a', usage)