import os
import sys
from os import listdir
from os.path import isfile, join


onlyfiles = [f for f in listdir('processed/') if isfile(join('processed/', f))]

print(onlyfiles)

for f in onlyfiles:
    f_no_extension = f.split(".")[0]
    string_command = "ffmpeg -i original/{} processed/{}.mp3"
    print(string_command, "String")
    command = f"ffmpeg -i processed/{f} unprocessed/{f_no_extension}.wav"
    print(command)
    os.system(command)
    delete_command = f"rm processed/{f_no_extension}.wav"
    os.system(delete_command)