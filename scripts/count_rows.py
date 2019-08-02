#!/usr/bin/env python

import sys
import json_lines

if __name__ == '__main__':

    try:

        file_name = str(sys.argv[1])
        count = 0

        with open(file_name, 'rb') as file:
            for item in json_lines.reader(file):
                count = count + 1

        print "number of rows in file: " + str(count)
        file.close()

    except:
        pass
