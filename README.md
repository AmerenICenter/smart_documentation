# Smart Documentation

Smart Documentation hopes to develop a pipeline to automatically generate documentation for Python libraries.

### Technologies:

- [Python]().
- [Sphinx]().
- [Virtualenv]().
- GitHub Actions

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
python populate_config.py
python docs/source/initial_write.py
cd docs, make html
```

### Tasks

- run commands on auto git push?

### Functionality

- The project to be documented is located in the `project` root directory.
- At the moment, all files with extension `.py` within the top level of the `project` folder shall be included into the docs. Does not work for nested python files yet.
