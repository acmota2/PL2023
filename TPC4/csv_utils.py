import re
from functools import reduce

def __media(l: list[int]) -> float:
    sum_: int = 0
    len_: int = 0
    for e in l:
        sum_ += e
        len_ += 1
    return sum_ / len_

__table = {
    'media': lambda l: __media([int(x) for x in l]),
    'sum': lambda l: sum([int(x) for x in l]),
    'maximum': lambda l: reduce(lambda x, y: x if x > y else y, [int(x) for x in l]),
    'minimum': lambda l: reduce(lambda x, y: x if x < y else y, [int(x) for x in l]),
    '': lambda x: x
}

def field_validation(field: str, raw: str, dispatcher: dict[dict], final_dict: dict) -> tuple[list, float]:
    m = dispatcher[field]
    if m != {} and 'range' in m and len(l := [x for x in raw.split(',') if x not in ['\n', '']]) in m['range']:
        if 'functions' in m:
            print(l)
            final_dict[f"{field}_{m['functions']}"] = __table[m['functions']](l)
    else:
        return None
    return final_dict

def make_match(header: str) -> tuple[str, dict]:
    regex = r'^'
    result_dispatcher = {}
    field_matcher = re.compile(r"((?P<field>[a-zA-ZÀ-ÖØ-öø-ÿ_]+)(\{(?P<range>\d+(,\d+)?)\})?(::(?P<function>media|sum|maximum|minimum))?)")
    for field, *_ in re.findall(field_matcher, header):
        if field != '':
            field_dispatcher = re.match(field_matcher, field).groupdict()
            field_name = field_dispatcher['field']
            result_dispatcher[field_name] = {}

            if field_dispatcher['range'] != None:
                span = [int(x) for x in field_dispatcher['range'].split(',')]
                result_dispatcher[field_name]['range'] = range(span[0], span[-1]+1)
                regex += fr"(?P<{field_dispatcher['field']}>([^,]*,?){{{field_dispatcher['range']}}})"

            else:
                regex += fr'(?P<{field}>[^,]*,?)'

            if field_dispatcher['function'] != None:
                result_dispatcher[field_name]['functions'] = (field_dispatcher['function'])

    regex += r'$'
    return regex, result_dispatcher
