import json

from dd_stuff import *
from SaveManager import SaveFileManager

# From 0 to 9 (or 8, you can see it in the profile save games folder)
PROFILE_NB = 1
# This will not be included, download it and put it in a .exclude folder here, or give whatever path you want
SAVE_EDITOR_JAR_PATH = ".exclude/DarkestDungeonSaveEditor-master/build/libs"
# My paths have been removed for security reasons
SAVE_PROFILES_FOLDER_PATH = ""
MOD_DIR_PATH = ""
# Don't change this, it is the correct target file for activating mods
TARGET_JSON = "persist.game.json"

MODLIST = "temp/modlist.csv"

if __name__ == '__main__':
    write_available_mods_csv(MOD_DIR_PATH, modlist_csv_to_list(MODLIST))

    sfm = SaveFileManager(SAVE_EDITOR_JAR_PATH, SAVE_PROFILES_FOLDER_PATH, PROFILE_NB)
    decrypted_path = sfm.decrypt_save_info(TARGET_JSON)
    with open(decrypted_path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        f.close()
        with open(decrypted_path, "w", encoding="utf-8") as f:
            json_data["base_root"]["applied_ugcs_1_0"] = convert_list_to_json_mods(modlist_csv_to_list(MODLIST))
            json_data["base_root"]["persistent_ugcs"]["applied_ugcs_1_0"] = json_data["base_root"]["applied_ugcs_1_0"]
            json.dump(json_data, f, indent=4)
            f.close()

    sfm.encrypt_save_info(TARGET_JSON)
