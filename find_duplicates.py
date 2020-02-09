#!/usr/bin/env python

import argparse
import sys
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


def filter_duplicates(dictionary):
    new_dictionary = {}
    for (key, value) in dictionary.items():
        if len(value) > 1:
            new_dictionary[key] = value
    return new_dictionary        

def find_duplicate_files(path):
    visited_files = {}
    visit_all_files(visited_files, path)
    just_duplicates = filter_duplicates(visited_files)
    pretty_print(just_duplicates)


def pretty_print(dictionary):
    for (key, values) in dictionary.items():
        print(key)
        for value in values:
            print(f"   {value}")
        print()    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find duplicate files')
    parser.add_argument('--path', '-p',
                       required=True,
                       help='the path to list')

    args = parser.parse_args()
    find_duplicate_files(args.path)