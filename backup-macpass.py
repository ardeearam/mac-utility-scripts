#!/usr/bin/env python3

#This script backups the Macpass database to AWS.

#Put this in the crontab like so:
# * * * * * /bin/zsh -lic "/usr/local/bin/backup-macpass.py" >> /Users/ardeearam/cronjob.log 2>>&1

import os
import subprocess

timestamp_process = subprocess.run(['date', '+%Y%m%d-%H%M%S'], check=True, text=True, stdout=subprocess.PIPE)
timestamp = timestamp_process.stdout.strip()
macpass_dest = os.getenv("MACPASS_DEST")
macpass_src = os.getenv("MACPASS_SRC")
macpass_destination_fullpath = f'{macpass_dest}/macpass-{timestamp}.kbx'
subprocess.run(['aws', 's3', 'cp', macpass_src , macpass_destination_fullpath, "--storage-class", "STANDARD_IA"], 
  check=True, text=True)