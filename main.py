from os import *

path_1 = "path" #path of file folder's
path_2 = "path" #path of folder where you want organize floders
extensions = ['.txt', '.png', '.jpg'] #extensions

for file in listdir(path_1):
    for ext in extensions:
        if file.endswith(ext):
            if path.exists(path_2 + "\{}".format(ext + "Files")):
                print("...")
                ext_folders = path_2 + "\{}".format(ext + "Files")
                rename(path_1 + "\{}".format(file), ext_folders + "\{}".format(file))
                print("success !")
            else:
                print("...")
                mkdir(path_2 + "\{}".format(ext + "Files"))
                print(path_2 + "\{}".format(ext + "Files"))
                ext_folders = path_2 + "\{}".format(ext + "Files")
                rename(path_1 + "\{}".format(file), ext_folders + "\{}".format(file))
                print("success !")
