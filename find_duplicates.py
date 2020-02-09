#!/usr/bin/env python

import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find duplicate files')
    parser.add_argument('--path', '-p',
                       required=True,
                       help='the path to list')


    args = parser.parse_args()