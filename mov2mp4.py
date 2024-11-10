#!/usr/bin/env python3

#This script converts MOV files (direct output of Mac video screenshot) into MP4 using ffmpeg.

import sys
import subprocess

try:
  old_filename = sys.argv[1]
  uuidgen_process = subprocess.run(['uuidgen'], check=True, text=True, stdout=subprocess.PIPE)
  new_filename = uuidgen_process.stdout.strip()
  print(old_filename)
  print(new_filename)
  ffmpeg_process = subprocess.run(f'ffmpeg -i "{old_filename}.mov" {new_filename}.mp4 && rm "{old_filename}.mov"', shell=True, check=True, text=True)
except IndexError:
  print('Usage: mov2mp4.py "screenshot 2024-11-11 at 7.39.33 AM"\n')