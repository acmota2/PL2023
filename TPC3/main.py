import re

def jsonify(raw: list[str], matcher):
    ...

def procs_year(registers: list[dict]) -> dict:
    result = {}
    matcher = re.compile(r'(\d+)')
    for person in registers:
        year = matcher.match(person['date']).groups(1)[0]
        if year not in result:
            result[year] = 0
        result[year] += 1
    return result

def name_surname(full_name: str, matcher) -> list[str]:
    result = re.findall(matcher, full_name)
    return [result[0], result[-1]] if len(result) != 1 else [result[0]]

def names_century(registers: list[dict]) -> dict:
    result = {}
    matcher = re.compile(r'(\d{2})')
    name_matcher = re.compile(r'([A-Z][a-z]+)')
    for person in registers:
        century = int(matcher.match(person['date']).groups(1)[0]) + 1
        if century not in result:
            result[century] = {'apelidos': {}, 'nomes': {}}
        
        all_names = [person['i'], person['mom'], person['dad']]
        for someone, _ in person['obs']:
            all_names.append(someone)
        
        for someone in all_names:
            h, *t = name_surname(someone, name_matcher)

            cur_name = result[century]['nomes']
            if h not in cur_name:
                cur_name[h] = 0
            cur_name[h] += 1

            cur_surname = result[century]['apelidos']
            if t:
                if t[0] not in cur_surname:
                    cur_surname[t[0]] = 0
                else:
                    cur_surname[t[0]] += 1
    return result

def verify_obs(person: dict, matcher) -> list[str]:
    if (obs := person['obs']) != '' and re.match(matcher, obs):
        obsl = []
        bla = re.findall(matcher, obs)
        for person, _, connection, _ in bla:
            obsl.append((person, connection))
        return obsl
    return []

def relations(registers: dict):
    result = {'Mãe': 0, 'Pai': 0}
    for person in registers:
        result['Mãe'] += 1
        result['Pai'] += 1
        if person['obs']:
            for _, con in person['obs']:
                if con not in result:
                    result[con] = 0
                result[con] += 1
    return result

if __name__ == '__main__':
    f = open('./processos.txt', 'r')
    proc = f.readlines()
    matcher = re.compile(r'^(?P<folder>\d+)::(?P<date>\d{4}-\d{2}-\d{2})::(?P<i>([A-Z][a-z]+\s)+[A-Z][a-z]+)::(?P<dad>([A-Z][a-z]+\s)+[A-Z][a-z]+)::(?P<mom>([A-Z][a-z]+\s)+[A-Z][a-z]+)::(?P<obs>.*)::$')
    matcher_obs = re.compile(r'(([A-Z][a-z]+\s?)+),(([A-Z][a-z]+\s?)+)')
    registers = []
    for line in set(proc):
        if re.match(matcher, line):
            person = matcher.search(line).groupdict()
            person['obs'] = verify_obs(person, matcher_obs)

            registers.append(person)
    
    print('Processes each year:')
    for year, freq in procs_year(registers).items():
        print(f'{year}: {freq}')

    for century, content in names_century(registers).items():
        print(f'\n{century} century:')
        print(f'names:')
        names = sorted(content['nomes'].items(), key=lambda x : x[1], reverse=True)
        for name, freq in names[:5]:
            print(f'{name}: {freq}')
        print(f'\nsurnames:')
        surnames = sorted(content['apelidos'].items(), key=lambda x : x[1], reverse=True)
        for surname, freq in surnames[:5]:
            print(f'{surname}: {freq}')

    print(f'\nRelations\' ocurrences:')
    for con, freq in relations(registers).items():
        print(f'{con}: {freq}')

    f = open('./rois.json', 'w')
    print('[', file=f)
    i: int = 0
    no_repeat = set(proc[:20])
    for line in no_repeat:
        if re.match(matcher, line):
            person = matcher.search(line).groupdict()
            print(f'''
    {{
        \"folder\": {person['folder']},
        \"date\": \"{person['date']}\",
        \"person\": \"{person['i']}\",
        \"mother\": \"{person['mom']}\",
        \"father\": \"{person['dad']}\",
        \"notes\": \"{person['obs']}\"
    }}{',' if i < len(no_repeat) - 1 else ''}''', file=f)
        i += 1
    print(']', file=f)
