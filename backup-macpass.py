#!/usr/bin/env python3

#This script backups the Macpass database to AWS.

import os
import subprocess

timestamp_process = subprocess.run(['date', '+%Y%m%d-%H%M%S'], check=True, text=True, stdout=subprocess.PIPE)
timestamp = timestamp_process.stdout.strip()
macpass_destination_fullpath = f'{os.getenv('MACPASS_DEST')}/macpass-{timestamp}.kbx'
subprocess.run(['aws', 's3', 'cp', os.getenv('MACPASS_SRC'), macpass_destination_fullpath, "--storage-class", "STANDARD_IA"], 
  check=True, text=True)