from sys import argv
import csv_utils as csv
from json import dumps
import re

if __name__ == '__main__':
    f = open(argv[1], 'r')
    h, *t = f.readlines()
    raw_matcher, dispatcher = csv.make_match(h)
    matcher = re.compile(raw_matcher)

    print(dispatcher)
    
    json_file = open(f"./{argv[1].split('.')[0]}.json", "w")
    dicts = []
    for line in t:
        current = '\t{\n'
        if m := matcher.fullmatch(line):
            line_strs = m.groupdict()
            print(line_strs)
            for k, v in line_strs.items():
                dispatcher = csv.field_validation(k, v, dispatcher)
            if dispatcher != None:
                dicts.append(dispatcher)
    final = dumps(obj=dicts, indent=2)
    print(final, file=json_file)