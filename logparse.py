#!/usr/bin/env python3
# Parse Windows Notepad ".LOG" files to csv

from sys import argv
import re
from pprint import pprint
from dateutil.parser import parse


input_file = argv[1]
output_file = argv[2]

with open(input_file, 'r') as f:
    input_text = f.read()

regex = re.compile(
    r'(?P<datetime>(?P<time>(\d+):(\d+) ([AP]M)) (?P<date>(\d+)/(\d+)/(\d+)))\n(?P<text>.*)', re.MULTILINE)

# matches = regex.findall(input_text)
# print(matches)
# output_text = re.sub(regex, r'\g<datetime>,\g<text>', input_text)
# print(output_text)

text_lines = [m.groupdict() for m in regex.finditer(input_text)]
csv_lines = ['{:%m/%d/%y %I:%M %p},{}\r\n'.format(parse(line['datetime']), line['text'])
             for line in text_lines]

with open(output_file, 'w') as f:
    f.write('Time,Description')
    f.writelines(csv_lines)
