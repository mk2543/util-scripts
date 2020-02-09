#!/usr/bin/env python

import argparse
from os import walk


def update_visited_file(visited_files, dir_path, file_name):
    path = to_path(dir_path, file_name)
    if file_name in visited_files:
        updated_paths= visited_files[file_name] + [path]
        visited_files[file_name] = updated_paths
    else:
        visited_files[file_name] = [path]

def to_path(dir_path, file_name):
    return f"{dir_path}/{file_name}"    


def visit_all_files(visited_files, path):
    for (dir_path, dirnames, filenames) in walk(path):
        for file_name in filenames:
            update_visited_file(visited_files, dir_path, file_name)


def find_duplicate_files(path):
    visited_files = {}
    visit_all_files(visited_files, path)
    print(visited_files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find duplicate files')
    parser.add_argument('--path', '-p',
                       required=True,
                       help='the path to list')

    args = parser.parse_args()
    find_duplicate_files(args.path)