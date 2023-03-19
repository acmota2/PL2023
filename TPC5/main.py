import coin
import re
from sys import stdin

def coin_checker(coins: list[str]) -> list[coin.coin]:
    ...


if __name__ == '__main__':
    while True:
        input('maq in touch> ')
        read: str = stdin.read()
        if re.match(r'^LEVANTAR$', read):
            print('')
        elif m := re.fullmatch(r'^MOEDA (?P<moedas>.*,?)+$'):
            coin_checker(m.groupdict()['moedas'].split(','))