import os
import re

dirName = ''
filePre = ''
fileLast = ''
delWord = '[壹高清]'

if __name__ == "__main__":
    dir = input("Enter dir: ")
    os.chdir(dir)
    print('working on dir: ' + os.getcwd())
    for count, f in enumerate(os.listdir()):
        f_name, f_ext = os.path.splitext(f)
        if f_name == 're_name':
            continue
        f_name = f_name.lstrip('0123456789.- ')
        strCount = str(count+1)+' '
        f_name = (filePre + strCount + f_name + fileLast).replace(delWord, '')

        new_name = f'{f_name}{f_ext}'
        os.rename(f, new_name)
