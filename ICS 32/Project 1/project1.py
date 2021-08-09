#Raul Cervantes 77825705
from pathlib import Path
import shutil

def user_interface():
    '''The user interface that runs all of the functions'''
    while True:
        try:
                first_order = input()
                
                if first_order[0] == "D":
                    Narrower(Directory(first_order[2:]))
                    return
                elif first_order[0] == "R":
                    Narrower(Recursive_printer(Recursive(first_order[2:])))
                    return
                else:
                    print("ERROR")
        except FileNotFoundError:
            print("ERROR")

def Narrower(files: list):
    '''Narrows down the options of the files that are in consideration'''

    while True:
        try:

            choices = input()

            if choices[0] == "A":
                if len(A(files)) == 0:
                    return
                else:
                    for i in A(files):
                        print(i)
                    Actions(A(files))
                    return
                
            elif choices[0] == "N" and len(choices) > 2:
                if len(N(files, choices[2:])) == 0:
                    return
                else:
                    for i in N(files, choices[2:]):
                        print(i)
                    Actions(N(files, choices[2:]))
                    return
                
            elif choices[0] == "E" and len(choices) > 2:
                if len(E(files, choices[2:])) == 0:
                    return
                else:
                    for i in E(files, choices[2:]):
                        print(i)
                    Actions(E(files, choices[2:]))
                    return
                
            elif choices[0] == "T" and len(choices) > 2:
                if len(T(files, choices[2:])) == 0:
                    return
                else:
                    for i in T(files, choices[2:]):
                        print(i)
                    Actions(T(files, choices[2:]))
                    return
                
            elif choices[0] == "<" and len(choices) > 2:
                if len(Less(files, int(choices[2:]))) == 0:
                    return
                else:
                    for i in Less(files, int(choices[2:])):
                        print(i)
                    Actions(Less(files, int(choices[2:])))
                    return
                
            elif choices[0] == ">" and len(choices) > 2:
                if len(More(files, int(choices[2:]))) == 0:
                    return
                else:
                    for i in More(files, int(choices[2:])):
                        print(i)
                    Actions(More(files, int(choices[2:])))
                    return
            else:
                print("ERROR")
        except ValueError:
            return

def Actions(files: list):
    """Take action on the files that were found"""

    while True:

        action = input()

        if action[0] == "F":
            F(files)
            return
        elif action[0] == "D":
            D(files)
            return
        elif action[0] == "T":
            t(files)
            return
        else:
            print("ERROR")
        
    

def Directory(path: str):
    '''Retrieves paths of directories, no subdirectories'''
    files = []

    p = Path(path)

    for directory in p.iterdir():
        if directory.is_file() == True:
            print(directory)
            files.append(directory)

    return files
    

def Recursive(path: str):
    '''All files in the directories and subdirectories and so forth'''
    all_files = []
    files = []
    subfiles = []

    p = Path(path)

    for directory in p.iterdir():
        if directory.is_file() == True:
            files.append(directory)
            files.sort()
        else:
            subfiles.append(directory)
            subfiles.sort()

    all_files.extend(files)

    for i in subfiles:
        all_files.extend(Recursive(i))

    return all_files

def Recursive_printer(file: list):
    '''Helps in storing the subdirectories into a list'''
    files = []

    files.extend(file)

    for i in files:
        print(i)

    return files

def A(files: list):
    '''All files are considered interesting'''

    return files

def N(files: list, file: str):
    '''Search files whose names match a particular name'''
    file_list = []
    for i in files:
        if i.name == file:
            file_list.append(i)

    return file_list
            
def E(files: list, suf: str):
    '''Search for files with a particular extension'''
    file_list = []
    for i in files:
        if suf[0] == '.' and suf == i.suffix:
            file_list.append(i)
        elif suf[0] != '.':
            suff = '.' + suf
            if suff == i.suffix:
                file_list.append(i)

    return file_list

def T(files: list, text: str):
    '''Search for text files that contain certain text'''
    file_list = []
    for i in files:
        if text in i.read_text():
            file_list.append(i)

    return file_list
    
def Less(files: list, byte: int):
    '''Search for files whose bytes is less than a certain number'''
    file_list = []
    for i in files:
        if int(i.stat().st_size) < byte:
            file_list.append(i)

    return file_list

def More(files: list, byte: int):
    '''Search for files whose bytes is more than a certain number'''
    file_list = []
    for i in files:
        if int(i.stat().st_size) > byte:
            file_list.append(i)

    return file_list

def F(files: list):
    '''print the first line of text from the file if it's a text file'''
    for i in files:
        if i.suffix == '.txt':
            f = i.open('r')
            line = f.readlines()
            print(line[0].strip("\n"))
        else:
            print('NOT TEXT')

def D(files: list):
    '''make a duplicate copy of a file and store it in the same directory'''
    for i in files:
        shutil.copy(i, str(i) + '.dup')

def t(files: list):
    '''modify its last modified timestamp to the current time/date'''
    for i in files:
        i.touch()
    
if __name__ == '__main__':
    user_interface()
