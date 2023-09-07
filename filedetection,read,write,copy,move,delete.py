import os

#path = insert your file/folder location here

#file detection
if os.path.exists(path):
    print("that location exists")
    if os.path.isfile(path):
        print("that is a file")
    elif os.path.isdir(path):
        print("that is directory!")
else:
    print("that location dosen't exist!")

#read a file
try:
    with open(test.txt) as file:
        print(file.read())
except FileNotFoundError:
    print("that file was not found :(")

#write a file

text = "Have a nice day! Cyaaaa"

with open('test.txt' , 'w','a') as file:
    file.write(text)

#copy a file

import shutil

shutil.copyfile('test.txt','copy.txt') #src.dst
.copy2

#move a file

import os

source = "test.txt"
destination=" file path "

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source + " Was not found")

#delete a file

import os
import shutil

path = "test.txt"

try:
    os.remove(path) #delete a file
    os.rmdir(path) #delete an empty directory
    shutil.rmtree(path) #delete a directory containing files
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("you do not have permission to delete that")
except OSError:
    print("you cannot delete that using that function")
else:
    print(path + " was deleted")