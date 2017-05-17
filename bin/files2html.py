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

parser = argparse.ArgumentParser(description="Reads the names of all .jpg files in a given directory, and creates an html fragment for the 365 homes page from them.")
parser.add_argument("dir", help="Name of input directory. Output file will be placed in the home directory of the current user and named 365fragment.html")
args = parser.parse_args()

directory = args.dir
outpath = join(expanduser("~"), "365fragment.html")
fout = open(outpath, "w+")

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".JPG") or filename.endswith(".JPEG"):
        basename, extension = splitext(filename)
        basename = basename.lstrip('0123456789.- ')
        fout.write (   "<div class=\"4u 12u$(mobile)\">" + "\n" + \
        			   "     <article class=\"item\">" + "\n" + \
        			   "        <div class=\"image fit\">" + "\n" + \
        			   "             <a href=\"images/365 homes/full/" + filename + "\" class=\"swipebox\" title=\"" + basename + "\">" + "\n" + \
                       "                <img src=\"images/365 homes/thumb/" + filename + "\" alt=\"image\">" + "\n" + \
        			   "		      </a>" + "\n" + \
        			   "		</div>" + "\n" + \
        			   "		<header>" + "\n" + \
        			   "		      <h3>" + basename + "</h3>" + "\n" + \
        			   "		</header>" + "\n" + \
        			   "	</article>" + "\n" + \
        			   "</div>" + "\n\n")
print("file written successfully to " + outpath)
fout.close()
