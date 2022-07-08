import sys
import os
sys.path.insert(0, os.path.abspath('../..'))
from project.load_config import instance

def write(file_name, mode, text):
    open(file_name, "w").close()
    f = open(file_name, mode)
    f.write(text)
    f.close()

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

for file_name in instance.files:
    index += "   " + file_name[:-3] + "\n"

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

Indices & Tables
----------------
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

active = """
.. note::

   This project is under active development.
"""

if instance.active:
    index += active

write(index_file_name, 'a', index)
write(usage_file_name, 'a', usage)

for file_name in instance.files:
    name = file_name[:-3]
    text = f""".. automodule:: project.{name}
    :members:
    """
    
    write(name + '.rst', 'a', text)