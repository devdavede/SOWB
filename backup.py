### SINGLE ONE WAY BACKUP ###

# !/usr/bin/python
import os
import os.path
import shutil
import logging
import sys
import integrity_checks

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def walk(current_directory, base_source_path, base_destination_path, integrity_algorithm_action):
    for path in os.listdir(current_directory):
        current_source_file = os.path.join(current_directory, path)

        if os.path.isdir(current_source_file):
            if path[0:1] == ".": continue
            walk(current_source_file, base_source_path, base_destination_path, integrity_algorithm_action)
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

        create_dir(target_path)

        if os.path.exists(target_file):
            logging.debug("! Exists !")
            if integrity_algorithm_action(current_source_file, target_file) == False:
                logging.debug("Comparison Algorithm Missmatch. Overwrite.")
                shutil.copy(current_source_file, target_file)
        else:
            logging.debug("Copy")
            shutil.copy(current_source_file, target_file)

        logging.debug("====")


if __name__ == "__main__":
    print("Hello")
    integrity_algorithm = "FILESIZE"
    if len(sys.argv) > 3:
        if sys.argv[4] == "MD5":
            integrity_algorithm = integrity_checks.INTEGRITY_ALGORITHM_MD5
        if sys.argv[4] == "FILESIZE":
            integrity_algorithm = integrity_checks.INTEGRITY_ALGORITHM_FILESIZE
        if sys.argv[4] == "MODIFICATIONDATE":
            integrity_algorithm = integrity_checks.INTEGRITY_ALGORITHM_MODIFICATION_DATE
        if sys.argv[4] == "FILENAME":
            integrity_algorithm = integrity_checks.INTEGRITY_ALGORITHM_FILENAME
        if sys.argv[4] == "NONE":
            integrity_algorithm = lambda: True

    if len(sys.argv) > 4:
        if sys.argv[4] == "DEBUG":
            logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        if sys.argv[4] == "INFO":
            logging.basicConfig(stream=sys.stderr, level=logging.INFO)
        if sys.argv[4] == "WARNING":
            logging.basicConfig(stream=sys.stderr, level=logging.WARN)

    print("Source: " + sys.argv[1])
    print("Destination: " + sys.argv[2])
    walk(sys.argv[1], sys.argv[1], sys.argv[2], integrity_algorithm)
