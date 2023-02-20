from db import db
from collections import defaultdict

class distribution:
    def __init__(self, db: db, field: str, insert_function = None):
        self.distribution = defaultdict(int)
        for person in db.db_content:
            key: str = person[field] if not insert_function else insert_function(person[field])
            self.distribution[key] + 1

    def __str__(self) -> str:
        rep: str = ''
        for k, v in self.distribution.items():
            rep += f'{k}: {v}\n'

    def __repr__(self) -> str:
        return str(self)