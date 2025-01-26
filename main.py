import os
import sys

mods_folders = sys.argv[1:]
used_files = {}
mods_folders = [f"{p}/{s}/" for p in mods_folders for s in os.listdir(p)]
for mods_folder in mods_folders:
    if not os.path.exists(mods_folder + "data"):
        continue
    nice_name = mods_folder.split("/")[-2]
    paths = []
    dirs = [f"data"]
    while len(dirs) != 0:
        dir = dirs.pop()
        new = os.listdir(mods_folder + dir)
        for path in new:
            path = f"{dir}/{path}"
            if os.path.isdir(mods_folder + path):
                dirs.append(path)
            else:
                paths.append(path)
    for path in paths:
        if path in used_files:
            used_files[path].append(nice_name)
        else:
            used_files[path] = [nice_name]

# print(used_files)
for path, users in used_files.items():
    if len(users) == 1:
        continue
    print(path, users)
