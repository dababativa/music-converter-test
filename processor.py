import os
import sys
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir('unprocessed/') if isfile(join('unprocessed/', f))]

print(onlyfiles)


# command = f"ffmpeg -i original/all-my-life.mp3 processed/all-my-life.mp3"
# os.system(command)