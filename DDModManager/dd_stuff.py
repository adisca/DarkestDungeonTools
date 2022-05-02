import os
import csv
from bs4 import BeautifulSoup


def get_mods(mod_dir_path):
    mods = []
    for dir_name in next(os.walk(mod_dir_path))[1]:
        dir_path = os.path.join(mod_dir_path, dir_name)
        for file in next(os.walk(dir_path))[2]:
            if file == "project.xml":
                file_path = os.path.join(dir_path, file)
                with open(file_path, encoding="utf8") as f:
                    file_contents = f.read()
                bs_data = BeautifulSoup(file_contents, "xml")
                mods.append(bs_data.find("Title").text)
                break
    return mods


def write_available_mods_csv(mod_dir_path, filter_modlist=None):
    if filter_modlist is None:
        filter_modlist = []
    with open("temp/available_mods.csv", "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.writer(f, delimiter=',')
        for mod in get_mods(mod_dir_path):
            if mod not in filter_modlist:
                csv_writer.writerow([mod])
        f.close()


def convert_list_to_json_mods(l):
    d = {}
    for i, mod in enumerate(l):
        d[f"{i}"] = {"name": mod, "source": "mod_local_source"}
    return d

def modlist_csv_to_list(modlist):
    l = []
    with open(modlist, encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        i = 0
        for row in csv_reader:
            if not (len(row) == 0 or row[0][0] == '#'):
                l.append(row[0])
                i += 1
        f.close()
    return l
