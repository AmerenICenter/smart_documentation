# gets function names from some file path

import sys
sys.path.append('../')
import calculator

function_names = [func for func in dir(calculator) if not func.startswith('__')]

print(function_names)