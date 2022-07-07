# Smart Documentation

Smart Documentation hopes to develop a pipeline to automatically generate documentation for Python libraries.

### Technologies:

- Python.
- [Sphinx]().
- [Virtualenv]().

### Run only once:

```
virtualenv venv: create virtual environment
venv\Scripts\activate: activate it
python -m pip install sphinx: install sphinx
sphinx-build --version: check the version? (not needed?)
sphinx-quickstart docs: create new Sphinx app (answer the default questions)
sphinx-build -b html docs/source/ docs/build/html: initial build
python docs/source/initial_write.py: run this to populate index.html file
cd docs, make html - every other time: on future Git pushes
```

### Run every time after the first:

```
virtualenv venv
venv\Scripts\activate
python docs/source/get_names.py
python docs/source/make_api.py
python docs/source/initial_write.py
python populate_config.py
cd docs, make html
```

### tasks

- make another make file which runs all the commands.
- run on auto git push?
- how to document classes/methods in classes/ and also errors (in addition to funcs)
- extract func names/etc directly from the files located in... some folder?
- does not work for nested py file . ( all python files must be in the root directory)
- autofunction, autoclass, etc.
- put name of file in the doc site for each page

### Functionality

- The project to be documented is located in the `project` root directory.
- At the moment, all files with extension `.py` within the top level of the `project` folder shall be included into the docs.
