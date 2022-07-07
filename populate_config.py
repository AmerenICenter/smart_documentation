# gets all the files in the 'project' directory

# import glob, os
# os.chdir("project")

# file_names = []

# for file in glob.glob("*.py"):
#     file_names.append(file)

# # function_names = [func for func in dir(commands) if not func.startswith('__')]

# print(file_names)

import os
import ast

project_name = 'project'

python_file_paths = []

for path, subdirs, files in os.walk(project_name):
    for name in files:
        current_file_path = os.path.join(path, name)
        if current_file_path[-2:] == "py":
            python_file_paths.append(current_file_path)

def find_methods_in_python_file(file_path):
    methods = []
    o = open(file_path, "r")
    text = o.read()
    p = ast.parse(text)
    for node in ast.walk(p):
        if isinstance(node, ast.FunctionDef):
            methods.append(node.name)

    return methods

res = {}

for file_path in python_file_paths:
    res[file_path] = (find_methods_in_python_file(file_path))

config_res = {}

for key in res:
    index = (key.rfind("\\")) + 1
    config_res[key[index:-3]] = res[key]

print(config_res)

del config_res['load_config']

name = "calculator"

# This will be the dictionary that determines our entire sphinx app:
config = {
    "project_name": name,
    "pip_package": name,
    "theme": "furo",
    "first_name": "Jacob",
    "last_name": "Chang",
    "year": "2022",
    "desc": "Calculator is a Python library for people who like to do mathematics.",
    "active": 1,
    "sections": {
      name: config_res
    }
}

import json

jsonString = json.dumps([config])
jsonFile = open("config.json", "w")
jsonFile.write(jsonString)
jsonFile.close()