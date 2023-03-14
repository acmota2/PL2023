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
    'media': lambda l: __media(l),
    'sum': lambda l: sum(l),
    'maximum': lambda l: reduce(lambda x, y: x if x > y else y, l),
    'minimum': lambda l: reduce(lambda x, y: x if x < y else y, l),
    '': lambda x: x
}

def field_validation(dispatcher: dict, line_groups: dict) -> tuple[list, float]:
    result = {}
    for field, raw in line_groups.items(): 
        l = [x for x in raw.split(',') if x != '']
        result[field] = raw
        if dispatcher[field] != {} and 'range' in dispatcher[field] and len(l) in dispatcher[field]['range']:
            result[field] = l = [int(x) for x in l]
            if 'functions' in dispatcher[field]:
                name = dispatcher[field]['functions']
                result[f"{field}_{name}"] = __table[name](l)
        elif 'range' in dispatcher[field] and len(l) not in dispatcher[field]['range']:
            return None

    return result

def make_match(header: str) -> tuple[str, dict]:
    regex = r'^'
    result_dispatcher = {}
    field_matcher = re.compile(r"((?P<field>[a-zA-ZÀ-ÖØ-öø-ÿ_]+)(\{(?P<range>\d+(,\d+)?)\})?(::(?P<function>media|sum|maximum|minimum))?)")
    for field, *_ in field_matcher.findall(header):
        if field != '':
            field_dispatcher = field_matcher.match(field).groupdict()
            field_name = field_dispatcher['field']
            result_dispatcher[field_name] = {}

            if field_dispatcher['range'] != None:
                span = [int(x) for x in field_dispatcher['range'].split(',')]
                result_dispatcher[field_name]['range'] = range(span[0], span[-1]+1)
                regex += fr"(?P<{field_dispatcher['field']}>([^,]*,?){{{field_dispatcher['range']}}})"

            else:
                regex += fr'((?P<{field}>[^,]*),?)'

            if field_dispatcher['function'] != None:
                result_dispatcher[field_name]['functions'] = (field_dispatcher['function'])

    regex += r'$'
    return regex, result_dispatcher
