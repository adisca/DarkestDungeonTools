import os
import shutil
from bs4 import BeautifulSoup
import lxml


def _dict_to_darkest_props(file_path, d):
    with open(file_path, "w") as f:
        line = [[], [], [], [], [], [], []]
        # order them based on the category, just in case it matters
        for l in d:
            # hall_curios: .chance 10 .types discarded_pack
            if d[l]['category'] == "hall_curios:":
                line[0].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")
            if d[l]['category'] == "room_curios:":
                line[1].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")
            if d[l]['category'] == "room_treasures:":
                line[2].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")
            if d[l]['category'] == "traps:":
                line[3].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")
            if d[l]['category'] == "obstacles:":
                line[4].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")
            if d[l]['category'] == "secret_room_treasures:":
                line[5].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")
            if d[l]['category'] == "prison_doors:":
                line[6].append(f"{d[l]['category']} .chance {d[l]['chance']} .types {l}\n")

        for i in line:
            for j in i:
                f.write(j)
            f.write("\n")
        f.close()


def _darkest_props_to_dict(darkest_file, d):
    if os.path.exists(darkest_file):
        f = open(darkest_file)
        for l in f.readlines():
            s = l.split()
            if len(s) == 5 and s[4] not in d:
                d[s[4]] = {"category": s[0], "chance": s[2]}
        f.close()


def get_target_mods(mod_dir_path):
    target_mods = []
    for dir_name in next(os.walk(mod_dir_path))[1]:
        if dir_name == "CuriosPatchMod":
            continue
        dir_path = os.path.join(mod_dir_path, dir_name)

        if os.path.exists(os.path.join(dir_path, "dungeons/cove/cove.props.darkest")) or \
                os.path.exists(os.path.join(dir_path, "dungeons/crypts/crypts.props.darkest")) or \
                os.path.exists(os.path.join(dir_path, "dungeons/warrens/warrens.props.darkest")) or \
                os.path.exists(os.path.join(dir_path, "dungeons/weald/weald.props.darkest")):
            target_mods.append([dir_path])
            for file in next(os.walk(dir_path))[2]:
                if file == "project.xml":
                    file_path = os.path.join(dir_path, file)
                    with open(file_path, encoding="utf8") as f:
                        file_contents = f.read()
                    bs_data = BeautifulSoup(file_contents, "xml")
                    target_mods[len(target_mods) - 1].append(bs_data.find("Title").text)
                    break
            if len(target_mods[len(target_mods) - 1]) < 2:
                target_mods[len(target_mods) - 1].append("Error getting title")
    return target_mods


def curio_patch(mod_dir_path, game_path, target_mods, overwrite_game_flag=False):
    cove = {}
    crypts = {}
    warrens = {}
    weald = {}

    if not overwrite_game_flag:
        _darkest_props_to_dict(os.path.join(game_path, "dungeons/cove/cove.props.darkest"), cove)
        _darkest_props_to_dict(os.path.join(game_path, "dungeons/crypts/crypts.props.darkest"), crypts)
        _darkest_props_to_dict(os.path.join(game_path, "dungeons/warrens/warrens.props.darkest"), warrens)
        _darkest_props_to_dict(os.path.join(game_path, "dungeons/weald/weald.props.darkest"), weald)

    for dir_path, title in target_mods:
        print(f"Adding {title} to the patch")
        _darkest_props_to_dict(os.path.join(dir_path, "dungeons/cove/cove.props.darkest"), cove)
        _darkest_props_to_dict(os.path.join(dir_path, "dungeons/crypts/crypts.props.darkest"), crypts)
        _darkest_props_to_dict(os.path.join(dir_path, "dungeons/warrens/warrens.props.darkest"), warrens)
        _darkest_props_to_dict(os.path.join(dir_path, "dungeons/weald/weald.props.darkest"), weald)

    if not os.path.exists(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/cove")):
        os.makedirs(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/cove"))
    if not os.path.exists(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/crypts")):
        os.makedirs(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/crypts"))
    if not os.path.exists(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/warrens")):
        os.makedirs(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/warrens"))
    if not os.path.exists(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/weald")):
        os.makedirs(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/weald"))

    _dict_to_darkest_props(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/cove/cove.props.darkest"), cove)
    _dict_to_darkest_props(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/crypts/crypts.props.darkest"), crypts)
    _dict_to_darkest_props(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/warrens/warrens.props.darkest"), warrens)
    _dict_to_darkest_props(os.path.join(mod_dir_path, "CuriosPatchMod/dungeons/weald/weald.props.darkest"), weald)

    shutil.copy2("resources/preview_icon.png", os.path.join(mod_dir_path, "CuriosPatchMod"))
    shutil.copy2("resources/project.xml", os.path.join(mod_dir_path, "CuriosPatchMod"))
