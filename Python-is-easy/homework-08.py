import os.path
from os import path

def createFile():
    file_name = input('Enter file name: ')

    if path.exists(file_name):
        action = input('Select your action. Write "r" to read, "w" to rewrite the content, and "a" to append text: ')

        if action == 'r':
            file = open(file_name, 'r')
            for line in file:
                print(line, end="")
        elif action == 'w':
            file = open(file_name, 'w')
            text = input('Write the new text: ')
            file.write(text)
        elif action == 'a':
            file = open(file_name, 'a')
            text = input('Write the text you want to append: ')
            file.write(' ' + text)
    else:
        file = open(file_name, 'w')
        text = input('Write the new text: ')
        file.write(text)
    file.close()

    
createFile()
