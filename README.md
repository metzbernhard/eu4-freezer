# eu4-freezer

###Update 13.12. didn't work as intended, because steam goes into the userdir to update the mods, so you're still left with incompatible mods. New version gives all mods an 'old-' prefix, to prevent Steam from updating them. 

Tool to save current state of EU4 installation

This tool helps you to "freeze" your current EU4 installation, so you can play old campaigns/mods after new versions arrived.

Select a) the Steam-Path containing the eu4.exe

b) the Documents/Paradox Interactive/Europa Universalis IV Path containing settings.txt

c) an empty(!) target directory\n        

The tool will copy the game in its current state, all savegames and all mods into the target directory.
Afterwards you can start the "frozen" version via the eu4.exe in the target directory.
If the DLC section is greyed out, you need to have steam running, while you start the game. 
This will in no way affect or be affected by changes by the your Steam-Installation for EU4.
After the copying is done, you can move the folder if you wish
    
    Command line usage: python freezeeu4-cli Path_to_eu4.exe Path_to_settings.txt Empty_Target_Path

![Screenshot](https://puu.sh/y9deT/4eaa8fdec4.png "Screenshot")
