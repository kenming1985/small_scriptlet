#!/usr/bin/python
#-*- coding: UTF-8 -*-
from __future__ import print_function
import os
import fnmatch
import tarfile
import datetime

def is_match_file(filename, patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

def find_specific_files(root, patterns=['*'], exclude_dirs=[]):
    for root, dirnames, filenames in os.walk(root):
        for filename in filenames:
            if is_match_file(filename, patterns):
                if not os.path.islink(os.path.join(root, filename)):
                    yield os.path.join(root, filename)
    for d in exclude_dirs:
        if d in exclude_dirs:
            os.remove(d)


def main():
    patterns= ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = "all_images_{0}.tar.gz".format(now)
    with tarfile.open(filename, 'w:gz') as f:
        for item in find_specific_files(".", patterns):
            f.add(item)


if __name__ == '__main__':
    main()
