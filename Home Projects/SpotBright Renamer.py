import os

StartRenaming == False

if StartRenaming == True:
    path = "c:/Users/Piotr/Pictures/SpotBright"
    for filename in os.listdir(path):
        for i in range(len(filename)):
            if filename[i] not in "0123456789":
                os.rename(path + '/' + filename, path + '/' + filename[i:])
                break
