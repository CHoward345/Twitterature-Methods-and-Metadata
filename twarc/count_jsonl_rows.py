import json_lines

val = raw_input("enter name of file: ")

count = 0

with open(val, 'rb') as f:
    for item in json_lines.reader(f):
        count = count + 1

print "number of rows in file: " + str(count)
f.close()
