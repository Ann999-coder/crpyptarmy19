import os

# define the name of the directory to be created
path = "kochi"

pat=os.getcwd()+"/kochi";
print(pat)
if os.path.isdir(pat):
    print("exists")
else:

    print("does not exists")
    os.mkdir(path)