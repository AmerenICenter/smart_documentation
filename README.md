# Smart Documentation

Smart Documentation hopes to develop a pipeline to automatically generate documentation for Python libraries.

### Technologies:

- [Python](https://www.python.org/).
- [Sphinx](https://www.sphinx-doc.org/en/master/).
- [Virtualenv](https://virtualenv.pypa.io/en/latest/).
- [GitHub Actions](https://github.com/features/actions).
- [GitHub Pages](https://pages.github.com/).

### First Time Usage

```
virtualenv venv
venv\Scripts\activate
python -m pip install sphinx
pip install -r requirements.txt
sphinx-build --version
sphinx-quickstart docs
sphinx-build -b html docs/source/ docs/build/html
create project/load_config.py
create populate_config.py & customize settings
create docs/source/initial_write.py
```

### Regular Usage

```
venv\Scripts\activate
make changes to source code
python populate_config.py
python docs/source/initial_write.py
make html within docs folder
```

### Tasks

- run commands on auto git push?
- run multiple commands in one line

### Information

- The project to be documented is located in the `project` root directory.
- Required files:

```
populate_config.py
docs/source/initial_write.py
project/load_config.py
```
