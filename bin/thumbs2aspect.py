#!/usr/bin/python -u

import os
import re
import sys
import argparse
import time
from os.path import expanduser
from os.path import join
from os.path import basename
from os.path import splitext
import datetime
from subprocess import call

parser = argparse.ArgumentParser(description="Converts all jpeg files in a directory to a given size, with white background padding. \
Assumes that a script 'aspect.sh' that does the actual conversion resides in the same directory as this script. \
Example: '~/bin/thumbs2aspect.py \"550x480\" .'")
parser.add_argument("widthxheight", help="width x height of output files")
parser.add_argument("in_dir", help="Name of input directory. Will be searched for jpeg files. Files will be replaced with resized ones.")
args = parser.parse_args()

path_to_current_script = os.path.dirname(os.path.realpath(__file__))
path_to_aspect_script = join(path_to_current_script, "aspect.sh")

for filename in os.listdir(args.in_dir):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG") or filename.endswith(".JPEG"):
        call([path_to_aspect_script, args.widthxheight, "-m", "pad", "-c","white", filename, join(args.in_dir, filename)])
print("Done.")
