#!/usr/bin/env python3

'''Parse Windows Notepad ".LOG" files to CSV.'''

from sys import argv
import re
from dateutil.parser import parse


def main():
    '''Read text from file, find timestamped events, and write as CSV.'''
    input_file = argv[1]
    output_file = argv[2]

    with open(input_file, 'r') as f:
        input_text = f.read()

    regex = re.compile(
        r'(?P<datetime>(\d+):(\d+) ([AP]M) (\d+)/(\d+)/(\d+))\n'
        r'(?P<text>.*)', re.MULTILINE)

    text_lines = [m.groupdict() for m in regex.finditer(input_text)]
    csv_lines = ['{:%m/%d/%y %I:%M %p},{}\r\n'.format(
        parse(line['datetime']), line['text']) for line in text_lines]

    with open(output_file, 'w') as f:
        f.write('Time,Description\r\n')
        f.writelines(csv_lines)


if __name__ == '__main__':
    main()
