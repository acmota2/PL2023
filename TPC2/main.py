import sys

if __name__ == '__main__':
    is_on: bool = True
    num_sum: int = 0
    while s := sys.stdin.read().lower():
        i: int = 0
        rep: str = ''
        len_s: int = len(s)
        while i < len_s:
            match s[i]:
                case 'o':
                    off_list: list[str] = [s[i+1], s[i+2]]
                    if i+1 < len_s and s[i+1] == 'n':
                        is_on = True
                        i += 1
                    elif all([x for x in map(lambda x: x < len_s, [i+1, i+2])]) and off_list == ['f', 'f']:
                        is_on = False
                        i += 2
                case '=':
                    num_sum += int(rep) if rep != '' else 0
                    print(num_sum)
                case other:
                    if is_on:
                        if s[i].isdigit():
                            rep += s[i]
                        if i+1 < len_s and not s[i+1].isdigit():
                            num_sum += int(rep) if rep != '' else 0
                            rep = ''
            i += 1
