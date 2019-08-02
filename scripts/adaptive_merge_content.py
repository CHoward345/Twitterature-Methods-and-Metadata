#!/usr/bin/env python

from __future__ import print_function

import jsonlines
import sys
import glob
import json_lines
import os

class parameters:

    searching_dirs  = 'searching for directories'
    adding_dirs     = 'adding {} to directory list'
    processing_dir  = 'looking under {} directory'
    less_arg_error  = 'function expects atleast two files'
    file_add_msg    = 'adding {}'
    file_open_msg   = 'opening {} in write mode'
    add_content_msg = 'adding content from {}'
    file_len_msg    = '{} contains {} elements'
    file_read_prog  = '{}/{} completed'
    end_msg         = 'content merged, closing output file'
    dir_level_up    = 'returning to main directory'

if __name__ == '__main__':

    try:

        list_directories = []
        print(parameters.searching_dirs)
        directories = os.listdir('.')
        print('\n')

        for directory in directories:
            if directory != 'adaptive_merge_content.py':
                print(parameters.adding_dirs.format(directory))
                list_directories.append(directory)
        print('\n')

        for directory in list_directories:

            print(parameters.processing_dir.format(directory))
            os.chdir('./{}'.format(directory))
            print('\n')

            list_files  = []

            for file in glob.glob('*.jsonl'.format(directory)):
                print(parameters.file_add_msg.format(file))
                list_files.append(file)

            if len(list_files) < 3:
                print(parameters.less_arg_error)
                break

            output_file = 'output.jsonl'.format(directory)
            print('\n')

            with jsonlines.open(output_file, mode = 'w') as writer:

                print(parameters.file_open_msg.format(output_file))
                print('\n')

                for file_name in list_files:
                    print(parameters.add_content_msg.format(file_name))
                    total_count = 0

                    with open(file_name, 'rb') as file:
                        for item in json_lines.reader(file):
                            total_count = total_count + 1

                    print(parameters.file_len_msg.format(file_name, total_count))
                    progress = 0

                    with jsonlines.open(file_name) as reader:
                        for item in reader:
                            writer.write(item)
                            progress = progress + 1
                            print(parameters.file_read_prog.format(progress, total_count), end = '\r')
                        reader.close()
                        print('\n')

                print(parameters.end_msg)
                writer.close()

            print(parameters.dir_level_up)
            print('\n')
            os.chdir('..')

    except:
        pass
