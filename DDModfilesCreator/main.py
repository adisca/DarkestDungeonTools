import os
import shutil

MOD_PATH = "YOUR_MODS_FOLDER_PATH/TARGET_MOD_FOLDER"


def create_modfiles(absolute_path, relative_path, lst):
    _, dirs, files = next(os.walk(absolute_path))
    for d in dirs:
        create_modfiles(os.path.join(absolute_path, d), os.path.join(relative_path, d).replace("\\", "/"), lst)
    for f in files:
        if f != "modfiles.txt":
            if relative_path == "":
                lst.append(f"{f} {os.path.getsize(os.path.join(absolute_path, f))}")
            else:
                lst.append(f"{relative_path}/{f} {os.path.getsize(os.path.join(absolute_path, f))}")


if __name__ == '__main__':
    lst = []
    create_modfiles(MOD_PATH, "", lst)
    with open("temp/modfiles.txt", "w", encoding="utf-8") as f:
        for line in lst:
            f.write(line)
            f.write("\n")
        f.close()
    with open("temp/modfiles.txt", "a", encoding="utf-8") as f:
        f.write(f"modfiles.txt {os.path.getsize('./temp/modfiles.txt') + 20 * 8}")
        f.close()

    shutil.copy2("temp/modfiles.txt", MOD_PATH)
