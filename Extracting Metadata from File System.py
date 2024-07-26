
import os
import time

def get_file_metadata(file_path):
    file_stats = os.stat(file_path)

    # File size
    file_size = file_stats.st_size

    # Permissions (simplified)
    file_permissions = oct(file_stats.st_mode)[-3:]

    # Timestamps
    creation_time = time.ctime(file_stats.st_ctime)
    last_modified_time = time.ctime(file_stats.st_mtime)
    last_accessed_time = time.ctime(file_stats.st_atime)

    # Print file metadata
    print(f"File: {file_path}")
    print(f"Size: {file_size} bytes")
    print(f"Permissions: {file_permissions}")
    print(f"Creation Time: {creation_time}")
    print(f"Last Modified Time: {last_modified_time}")
    print(f"Last Accessed Time: {last_accessed_time}")

# Example usage
file_path = 'example.txt'
get_file_metadata(file_path)
