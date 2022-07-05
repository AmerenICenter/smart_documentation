def write(file_name, mode, text):
    open(file_name, "w").close()
    f = open(file_name, mode)
    f.write(text)
    f.close()