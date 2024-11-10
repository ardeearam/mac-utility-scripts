#!/usr/bin/env python3

import sys
import subprocess

old_filename = sys.argv[1]
uuidgen_process = subprocess.run(['uuidgen'], check=True, text=True, stdout=subprocess.PIPE)
new_filename = uuidgen_process.stdout.strip()
print(old_filename)
print(new_filename)
ffmpeg_process = subprocess.run(f'ffmpeg -i "{old_filename}.mov" {new_filename}.mp4 && rm "{old_filename}.mov"', shell=True, check=True, text=True)
