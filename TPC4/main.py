from sys import argv
import csv_utils as csv
import re

if __name__ == '__main__':
    f = open(argv[1], 'r')
    h, *t = f.readlines()
    raw_matcher, dispatcher = csv.make_match(h)
    matcher = re.compile(raw_matcher)

    print(dispatcher)
    
    json = open(f"./{argv[1].split('.')[0]}.json", "w")
    final = f'[\n'
    for line in t:
        current = '\t{\n'
        if m := matcher.fullmatch(line):
            line_strs = m.groupdict()
            print(line_strs)
            for k, v in dispatcher.items():
                if (valid := csv.field_validation(k, v, dispatcher, line_strs)) != None:
                    print(valid)