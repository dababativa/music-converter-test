import os
import sys
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir('unprocessed/') if isfile(join('unprocessed/', f))]

print(onlyfiles)

for f in onlyfiles:
    no_extension_name = f.split(".")[0]
    command = f"ffmpeg -i original/{} processed/{}.mp3".format(f,no_extension_name)
    print(command)
    os.system(command)