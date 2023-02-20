from db import db
from distribution import distribution
from threading import Thread
from typing import Callable

def disease_by_sex(db: db) -> distribution:
    return distribution(db, 'sex')

def disease_by_age_group(db: db) -> distribution:
    grouper = lambda k: f'{(k // 5) * 5}-{((k // 5) * 5) + 4}'
    return distribution(db, 'age', grouper)

def disease_by_colesterol(db: db) -> distribution:
    grouper = lambda k: f'{(k // 10) * 10}-{((k // 10) * 10) + 9}'
    return distribution(db, 'colesterol', grouper)

def read_csv(file) -> list[str]:
    _, *content = file.readlines()
    return content

def distribution_execution(data_base: db, function: Callable[[db], distribution]):
    dist: distribution = function(data_base)
    print(dist)
    dist.show_distribution()

if __name__ == '__main__':
    file = open('myheart.csv', 'r')
    data_base = db(read_csv(file))
    distribution_execution(data_base, disease_by_sex)
    distribution_execution(data_base, disease_by_age_group)
    distribution_execution(data_base, disease_by_colesterol)
