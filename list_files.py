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

print(res)