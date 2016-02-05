#by pythonwriter(github)
#python 3
import sys
import os
def Cont():
 start = input('what do you want to do? \n')
 if start == 'make file':
    fileName = input('Name of file to make: ')
    file = open(fileName, 'a')
    add = input('do you want to add text to it? Y or N\n')
    if add == 'Y':
        write = input('what to add: ')
        file.write(write)
        Cont()
    else:
        bye = input('ok!')
        Cont()
 elif start == 'delete file':
    fileN = input('file to delete PATH: ')
    os.remove(fileN)
    Cont()
 elif start == 'read file':
    filen = input('file to read name: ')
    FILE = open(filen, encoding='utf-8')
    print(FILE.read())
    Cont()
 elif start == 'quit':
     sys.exit(0)
 elif start == 'read binary':
     binA = input('which binary file: ')
     Bfile = open(binA, encoding='utf-8')
     print(Bfile.read())
     Cont()
 elif start == 'help':
     print('ERROR NO 1 = incorrect command')
     Cont()
 else:
     error = input('ERROR NO.1')
     Cont()
Cont()
