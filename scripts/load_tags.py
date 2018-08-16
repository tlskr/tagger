#!/usr/bin/env python
# pylint: disable=wrong-import-position

"""
Script loading tags from JSON file to data

Invocation (from project root)

    ./scripts/load_tags.py
"""

import os
import sys

import gflags

sys.path.append(os.getcwd())

from scripts.main_gflag import main_gflagged

from tagger.load_json import insert_tags


FLAGS = gflags.FLAGS

gflags.DEFINE_string(
    "datafile", None, "file holding json data"
)



def main():
    insert_tags(FLAGS.datafile)



if __name__ == "__main__":
    sys.exit(main_gflagged(sys.argv, main))
