# !/usr/bin/python
import os
import os.path
import hashlib
import shutil
import logging
import sys

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def walk(current_directory, base_source_path, base_destination_path):
    for path in os.listdir(current_directory):
        current_source_file = os.path.join(current_directory, path)
        if path[0:1] == ".":
            continue

        if os.path.isdir(current_source_file):
            walk(current_source_file, base_source_path, base_destination_path)
            continue

        relative_source_path = current_source_file[len(base_source_path):]
        target_file = base_destination_path + relative_source_path
        target_path = os.path.dirname(target_file)

        logging.debug("Checking Directory: " + current_directory)
        logging.debug("Source Base Path: " + base_source_path)
        logging.debug("Source File: " + current_source_file)
        logging.debug("Source Path relative to starting path: " + relative_source_path)
        logging.debug("Target Path:" + target_path)
        logging.debug("Target File:" + target_file)
        logging.debug("====")

        create_dir(target_path)

        if os.path.exists(target_file):
            md5_source = hashfile(current_source_file)
            md5_target = hashfile(target_file)
            if md5_source != md5_target:
                shutil.copy(current_source_file, target_file)
        else:
            shutil.copy(current_source_file, target_file)

def hashfile(file):
    BLOCK_SIZE = 65536
    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)
    return file_hash.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        walk(sys.argv[2], sys.argv[2], sys.argv[3])

    if len(sys.argv) == 4:
        if sys.argv[4] == "DEBUG":
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        if sys.argv[4] == "INFO":
            logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        if sys.argv[4] == "WARNING":
            logging.basicConfig(stream=sys.stderr, level=logging.WARN)
