from db import db

def decease_by_sex(data: db) -> tuple[int, int]:
    ...

def read_csv(file) -> list[str]:
    return file.lines()

if __name__ == '__main__':
    file = open('myheart.csv', 'r')
    _, *content = read_csv(file)
    data_base = db(content)
