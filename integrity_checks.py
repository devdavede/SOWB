# !/usr/bin/python

### INTEGRITÄTSALGORITHMEN ###
# Return TRUE if Files match
# Return FALSE if Files do not match
##############################

import os
import os.path
import hashlib

def hashfile(file):
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()

def INTEGRITY_ALGORITHM_MD5(src, target):
    md5_source = hashfile(src)
    md5_target = hashfile(target)
    return md5_source == md5_target

def INTEGRITY_ALGORITHM_FILESIZE(src, target):
    return os.stat(src).st_size == os.stat(target).st_size

def INTEGRITY_ALGORITHM_MODIFICATION_DATE(src, target):
    return os.path.getmtime(src) == os.path.getmtime(target)

def INTEGRITY_ALGORITHM_FILENAME(src, target):
    return os.path.basename(src) == os.path.basename(target)