import os
from pathlib import  Path

# Create file if it doesn't exists to avoid FileNotFoundError exception
dir_names = 'Names'
file_name = 'contri.txt'
if not  Path(file_name).exists():
    Path(file_name).touch()

# Get filename and split it
for i in [x.stem for x in Path(dir_names).iterdir()]:
    name, username = str(i).split(',')
    word = name+username
    with open(file_name) as file:
        file = file.read()

        # Make sure line isn't written
        if word not in file:
            fr = open(file_name, 'a')
            fr.write(word+"\n")
            fr.close()
# Just to check if file was written
check =  Path(file_name).read_text()
print(check)
