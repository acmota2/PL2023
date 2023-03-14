from sys import argv
import csv_utils as csv2
from json import dumps
import re

if __name__ == '__main__':
    f = open(argv[1], 'r')
    h, *t = f.readlines()
    raw_matcher, dispatcher = csv2.make_match(h)
    matcher = re.compile(raw_matcher)
    json_file = open(f"./{argv[1].split('.')[0]}.json", "w")
    dicts = []
    for line in [x.rstrip('\n') for x in t]:
        if m := matcher.fullmatch(line):
            line_strs = m.groupdict()
            maybe_valid = csv2.field_validation(dispatcher, line_strs)

            if maybe_valid != None:
                dicts.append(maybe_valid)

    final = dumps(obj=dicts, indent=4, ensure_ascii=False)
    print(final, file=json_file)
