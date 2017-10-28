import shutil
import os
import sys
from distutils.dir_util import copy_tree


def check():
    '''checks if the paths could be correct'''
    paths_correct = True
    if not os.path.isfile(sys.argv[1] + '\eu4.exe'):
        paths_correct = False
        print("Your EU4 path is wrong!")
    if not os.path.isfile(sys.argv[2] + '\settings.txt'):
        paths_correct = False
        print("Your Settings path is wrong!")
    # print(os.listdir(self.paths[self.path3]))
    if not os.listdir(sys.argv[3]) == []:
        paths_correct = False
        print("Your Target path is not empty!")
    return paths_correct


def finish():
    if not check():
        return
    checked = True
    if checked:
        os.chdir(sys.argv[3])
        copy_tree(sys.argv[1], sys.argv[3])
        with open('userdir.txt', 'w+') as file:
            file.write('.')
        if not os.path.isdir('save games'):
            os.mkdir('save games')
        if not os.path.isdir('mod'):
            os.mkdir('mod')
        copy_tree(sys.argv[2] + '\mod', sys.argv[3] + '\mod')
        copy_tree(sys.argv[2] + '\save games', sys.argv[3] + '\save games')
        shutil.copy(sys.argv[2] + '\settings.txt', sys.argv[3] + '\settings.txt')
        print('Copy finished, enjoy!')
    else:
        print("Please check your Paths.")


def main():

    helptext = '''
    This tool helps you to "freeze" your current EU4 installation, so you can play old campaigns/mods after new versions arrived.\n
    Select a) the Steam-Path containing the eu4.exe
    b) the Documents/Paradox Interactive/Europa Universalis IV Path containing settings.txt
    c) an empty(!) target directory\n        
    The tool will copy the game in its current state, all savegames and all mods into the target directory.
    Afterwards you can start the "frozen" version via the eu4.exe in the target directory.
    If the DLC section is greyed out, you need to have steam running, while you start the game. 
    This will in no way affect or be affected by changes by the your Steam-Installation for EU4.
    After the copying is done, you can move the folder if you wish
    
    Command line usage: python freezeeu4-cli Path_to_eu4.exe Path_to_settings.txt Empty_Target_Path'''

    try:
        if sys.argv[1] == 'help':
            print(helptext)
            sys.exit()
    except IndexError:
        print('No arguments given! Type "python freezeeu4-cli.py help" for Information on usage')
        sys.exit()

    if len(sys.argv) != 4:
        print('Incorrect amount of Arguments. Correct usage: '
              'python freezeu4-cli.py EU4-Path Settings-Path Target-Path\n'
              'type "python freezeeu4-cli.py help" for more information')
        sys.exit()
    finish()


if __name__ == "__main__":
    main()
