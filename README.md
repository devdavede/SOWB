# SOWB - Simple One Way Backup

## Overview
This Python script facilitates the synchronization of files and directories from a source location to a destination location. It employs checksum verification to identify changes and copies only the modified files, ensuring efficient synchronization.

## Features
- **Directory Traversal**: Walks through directories recursively to identify files and directories for synchronization.
- **Checksum Comparison**: Utilizes SHA-256 hashing to compare files, ensuring accurate detection of modifications.
- **Logging**: Offers logging functionality to track the synchronization process and debug potential issues.
- **Customizable Behavior**: Supports command-line arguments for specifying logging level and source/destination paths.

## Prerequisites
- Python 3.x installed on the system.

## Usage
- Command-Line Arguments:
  - `python script_name.py [source_path] [destination_path] [logging_level]`
    - `source_path`: Path to the source directory.
    - `destination_path`: Path to the destination directory.
    - `logging_level` (optional): Specify logging level (`DEBUG`, `INFO`, or `WARNING`).

**Example**:
   ```bash
   python3 backup.py /path/to/source /path/to/destination DEBUG
  ````
## Script Structure
- **`create_dir(path)`:** Creates a directory if it does not exist.
- **`walk(current_directory, base_source_path, base_destination_path)`:** Recursively traverses directories, comparing and synchronizing files. I assume no liability for this code.
- **`hashfile(file)`:** Computes the SHA-256 hash of a file.
- **`if __name__ == "__main__":` Block:** Handles command-line arguments and initiates the synchronization process.

## Notes
- Ensure proper permissions for reading from the source directory and writing to the destination directory.
- Use caution when synchronizing files, especially in production environments, to avoid data loss or corruption.
