from load_config import instance

# returns a dictionary with everything being documented in this project:
# {
    # "file_name": <[list of properly formatted autofunction names]>
# }

docs = instance.docs
func_results = {} # functions to be documented
# number of files to be documented
number_of_files = 0
file_names = []

for doc in docs:
    file_name = list(doc.keys())[0]
    function_names = doc[file_name]
    formatted_func_names = []
    for name in function_names:
        formatted_func_names.append('.. autofunction:: calculator.' + str(name))
    number_of_files += 1
    func_results[file_name] = formatted_func_names
    file_names.append(file_name + '.rst')

# print(func_results)
# print(number_of_files)