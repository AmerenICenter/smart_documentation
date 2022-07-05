import glob, os
os.chdir("folder")
for file in glob.glob("*.py"):
    print(file)