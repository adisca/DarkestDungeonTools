# DarkestDungeonTools
As you may know, the Steam version of the game Darkers Dungeon has access to the incredibly useful Steam Workshop, and versions like the GOG one (which I have) are barred from the wonderful world of modding. I created a few tools for personal use and wanted to share them with the world.
They require Python3 to run.
DON'T JUST RUN THEM OUT OF THE BOX! They were tailor-made for myself, take a second and look in the main.py file at the globals.
It uses "defines" (just globals in Python I guess) that you may change with your own paths.

# DDCuriosPatcher
When it comes to curios, DD mods have always had compatibility issues and required separate patches mods or awkward workarounds.
Now you no longer have to trouble yourself with this
This program looks into your mods folder for all mods that add new curios and creates a new patch mod that combines all of them.
As this is my lates tool, the user experience is improved and you have multiple options 

# DDModfilesCreator
This simple programs creates a modfiles.txt file for your chosen mod.
Steam Workshop does it automatically and, while not required (at least from my tests), the game may use it if it exists.
Now you can do it with ease too. The modfiles.txt is generated in a temp folder, so manually copy it in the mod folder (for safety it doesn't directly overwrite it in the mod folder).

# DDModManager
A crude mod manager.
It generates a list of all your available mods in a available_mods.csv file from where you can copy them in a modlist.csv. It takes into consideration the order too, because this was the main reason I created it. An example with explenations is provided.
You need to have an existing profile that has started the game. You can just start the "Old Road" tutorial mission and not leave the first room (or just ALT+F4 once the loading screen has finished loading) and that is enough.
ANY MOD THAT MUST BE ENABLED ON A CLEAN PROFILE MUST BE DONE SO MANUALLY!

This mod utilizes the DarkestDungeonSaveEdittor, made by robojumper found at https://github.com/robojumper/DarkestDungeonSaveEditor.
You need to download it and provide the path in the code defines.

# As the license states, you are free to use them however you want and I am not held accountable for anything that may go wrong
