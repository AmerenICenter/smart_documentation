from load_config import instance

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
   api
"""

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

def write(file_name, mode, text):
    open(file_name, "w").close()
    f = open(file_name, mode)
    f.write(text)
    f.close()

write(index_file_name, 'a', index)
write(usage_file_name, 'a', usage)

api_file_name = 'api.rst'

section_names = [list(instance.docs[0].keys())[0], list(instance.docs[1].keys())[0]]
function_names = list(instance.docs[0].values())[0]
print(function_names)
api_text = """
API
*********

"""
for name in function_names:
    api_text += ('.. autofunction:: calculator.' + str(name) + "\n")

print(api_text)
write(api_file_name, 'a', api_text)
# api_text = """
# Creating recipes
# ----------------
# .. autofunction:: lumache.get_random_ingredients
# .. autofunction:: lumache.get_random_ingredients
# .. autofunction:: lumache.get_random_ingredients

# .. autoexception:: lumache.InvalidKindError

# """


# Creating recipes
# ----------------

# To retrieve a list of random ingredients,
# you can use the ``lumache.get_random_ingredients()`` function:

# .. autofunction:: lumache.get_random_ingredients

# The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
# or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
# will raise an exception.

# .. autoexception:: lumache.InvalidKindError