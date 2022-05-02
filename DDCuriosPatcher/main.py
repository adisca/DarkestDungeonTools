from dd_lib import *
from termcolor import colored


MODS_DIR_PATH = "C:/Games/Darkest Dungeon Ancestral Edition/mods"
GAME_DIR_PATH = "C:/Games/Darkest Dungeon Ancestral Edition"

if __name__ == '__main__':
    target_mods = get_target_mods(MODS_DIR_PATH)

    while True:
        print(colored("Detected mods that add or change curios", "yellow"))
        for i, [_, name] in enumerate(target_mods):
            print(i, name)
        cmd = input(colored("Write index to remove, or -1 to patch: ", "blue"))
        try:
            cmd = int(cmd)
        except ValueError:
            print(colored("Invalid input", "red"))
            continue
        if cmd == -1:
            break
        else:
            if 0 <= cmd < len(target_mods):
                _, name = target_mods.pop(cmd)
                print(colored(f"Removed {name}", "green"))
            else:
                print(colored("Index out of range", "red"))

    # this is in place of a proper ordering functionality
    overwrite_game_flag = False
    while True:
        cmd = input(colored("Overwrite base game curios? [y]es/[n]o: ", "blue"))
        if cmd == "y" or cmd == "yes":
            overwrite_game_flag = True
            while True:
                for i, [_, name] in enumerate(target_mods):
                    print(i, name)
                cmd = input(colored("Mod index to overwrite base, -1 to not overwrite: ", "blue"))
                try:
                    cmd = int(cmd)
                except ValueError:
                    print(colored("Invalid input", "red"))
                    continue
                if cmd == -1:
                    overwrite_game_flag = False
                    break
                else:
                    if 0 <= cmd < len(target_mods):
                        mod = target_mods.pop(cmd)
                        target_mods.insert(0, mod)
                        print(colored(f"Chose {mod[1]} as base", "green"))
                        break
                    else:
                        print(colored("Index out of range", "red"))
            break
        if cmd == "n" or cmd == "no":
            overwrite_game_flag = False
            break
        print(colored("Invalid input", "red"))

    print(colored("Generating patch with settings: ", "yellow"))
    print(colored("Mods:", "yellow"))
    for _, name in target_mods:
        print("\t", name)
    print(colored(f"Overwrite base game: ", "yellow") + str(overwrite_game_flag))
    if overwrite_game_flag:
        print(colored("Mod used as new base: ", "yellow"), target_mods[0][1])

    curio_patch(MODS_DIR_PATH, GAME_DIR_PATH, target_mods, overwrite_game_flag)
    print(colored("Done", "green"))
