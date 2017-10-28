import shutil
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
from distutils.dir_util import copy_tree


class gui:
    def __init__(self, window):
        self.window = window
        self.window.title('EU4 Freezer')
        self.style = ttk.Style()
        self.paths = {}
        self.helptext = '''
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
        # self.mods=['All Mods', 'Selected Mods']

        # EU4 Path Section
        ttk.Label(self.window, text='EU4 Path:').grid(row=0, column=0, pady=3, padx=5, sticky='e')
        # Entry
        self.path1 = ttk.Entry(self.window, width=30)
        self.path1.grid(row=0, column=1, pady=3)
        # Button
        self.button1 = ttk.Button(self.window, text='Select Path...', command=lambda: self.path(self.path1))
        self.button1.grid(row=0, column=2, pady=3, padx=5)

        ttk.Separator(self.window, orient=HORIZONTAL).grid(row=1, column=0, sticky='ew', columnspan=3)

        # Selectings-Path Section
        ttk.Label(self.window, text='Settings Path:').grid(row=2, column=0, pady=3, padx=5, sticky='e')
        # Entry
        self.path2 = ttk.Entry(self.window, width=30)
        self.path2.grid(row=2, column=1, pady=3)
        # Button
        self.button2 = ttk.Button(self.window, text='Select Path...', command=lambda: self.path(self.path2))
        self.button2.grid(row=2, column=2, pady=3, padx=5)

        ttk.Separator(self.window, orient=HORIZONTAL).grid(row=3, column=0, sticky='ew', columnspan=3)

        # Target-Path Section
        ttk.Label(self.window, text='Target Path').grid(row=4, column=0, pady=3, padx=5, sticky='e')
        # Entry
        self.path3 = ttk.Entry(self.window, width=30)
        self.path3.grid(row=4, column=1, pady=3)
        # Button
        self.button3 = ttk.Button(self.window, text='Select Path...', command=lambda: self.path(self.path3))
        self.button3.grid(row=4, column=2, pady=3, padx=5)

        ttk.Separator(self.window, orient=HORIZONTAL).grid(row=5, column=0, sticky='ew', columnspan=3)

        self.finish_button = ttk.Button(self.window, text='Finish!', command=lambda: self.finish())
        self.finish_button.grid(row=6, column=2, pady=3, padx=5, sticky='e')
        self.help_button = ttk.Button(self.window, text='Help me!', command=lambda: self.help())
        self.help_button.grid(row=6, column=0, pady=3, padx=5, sticky='w')

    def path(self, path):
        """Asks Directory for EU4"""
        folder = filedialog.askdirectory()
        # print(self.path1)
        path.delete(0, END)
        path.insert(0, folder)
        self.paths[path] = folder
        print(self.paths)

    def finish(self):
        if not self.check():
            return
        check = (len(self.paths) == 3)
        for path in self.paths.values():
            # print(path)
            check = check & os.path.isdir(path)
            # print(check)
        if check:
            os.chdir(self.paths[self.path3])
            copy_tree(self.paths[self.path1], self.paths[self.path3])
            with open('userdir.txt', 'w+') as file:
                file.write('.')
            if not os.path.isdir('save games'):
                os.mkdir('save games')
            if not os.path.isdir('mod'):
                os.mkdir('mod')
            copy_tree(self.paths[self.path2] + '\mod', self.paths[self.path3] + '\mod')
            copy_tree(self.paths[self.path2] + '\save games', self.paths[self.path3] + '\save games')
            shutil.copy(self.paths[self.path2] + '\settings.txt', self.paths[self.path3] + '\settings.txt')
            messagebox.showinfo(title='Done!', message='Copy finished, enjoy!')
        else:
            messagebox.showerror(title="Something went wrong",
                                 message="Please check your Paths.")

    def check(self):
        '''checks if the paths could be correct'''
        paths_correct = True
        if not os.path.isfile(self.paths[self.path1] + '\eu4.exe'):
            paths_correct = False
            messagebox.showerror(title="Something went wrong",
                                 message="Your EU4 path is wrong!")
        if not os.path.isfile(self.paths[self.path2] + '\settings.txt'):
            paths_correct = False
            messagebox.showerror(title="Something went wrong",
                                 message="Your Settings path is wrong!")
        # print(os.listdir(self.paths[self.path3]))
        if not os.listdir(self.paths[self.path3]) == []:
            paths_correct = False
            messagebox.showerror(title="Something went wrong",
                                 message="Your Target path is not empty!")
        return paths_correct

    def help(self):
        messagebox.showinfo('How to Use', self.helptext)


def main():
    window = Tk()
    freeze = gui(window)
    window.mainloop()


if __name__ == "__main__":
    main()
