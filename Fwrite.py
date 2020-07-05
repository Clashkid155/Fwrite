import os, sys
from pathlib import  Path

#Get arguments
ag = len(sys.argv) -1
if ag != 2:
    sys.exit("Not enough parameter supplied")

# Create file if it doesn't exists to avoid FileNotFoundError exception
dir_names = sys.argv[1]
file_name = sys.argv[2]
if not Path(file_name).exists():
    Path(file_name).touch()

# Get filename without extension and directory
for i in [x.stem for x in Path(dir_names).iterdir() \
          if not Path(x).is_dir()]:
    word = str(i)

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
