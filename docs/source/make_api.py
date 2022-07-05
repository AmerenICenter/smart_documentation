# api_file_name = 'api.rst'

# section_names = [list(instance.docs[0].keys())[0], list(instance.docs[1].keys())[0]]
# function_names = list(instance.docs[0].values())[0]
# print(function_names)
# api_text = """
# API
# *********

# """
# for name in function_names:
#     api_text += ('.. autofunction:: calculator.' + str(name) + "\n")

# print(api_text)
# write(api_file_name, 'a', api_text)

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/modules')

from modules import file_write

import get_names
# print(get_names.file_names)

for file_name in get_names.file_names:
    text = usage = f"""
    hello world
"""
    file_write.write(file_name, 'a', text)