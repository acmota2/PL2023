import matplotlib.pyplot as plt
from db import db
from typing import Callable, Any

class distribution:
    def __init__(self, db: db, key: str, key_func: Callable[[Any], str] = None):
        self.dist: dict = {}
        self.key = key
        if key_func == None:
            for person in db.db_content:
                new_key = person.data_fields[key]
                if new_key not in self.dist:
                    self.dist[new_key] = [0, 0]
                i: int = 1 if person.data_fields['has_disease'] else 0
                self.dist[new_key][i] += 1
        else:
            for person in db.db_content:
                new_key = key_func(person.data_fields[key])
                if new_key not in self.dist:
                    self.dist[new_key] = [0, 0]
                i: int = 1 if person.data_fields['has_disease'] else 0
                self.dist[new_key][i] += 1

    def __str__(self) -> str:
        rep: str = ''
        rep += f'distribution by {self.key}\n[has disease]\t[doesn\'t have disease]\n'
        
        for k, v in self.dist.items():
            rep += f'{k}: {v[0]} {v[1]}\n'
        return rep

    def __repr__(self) -> str:
        return str(self)

    def show_distribution(self):
        plt.figure(figsize=(9, 3))
        plt.title(label=f'Distribution by {self.key}')
        bars = []
        for k, v in self.dist.items():
            bars.append((f'{k}\nno disease', v[0]))
            bars.append((f'{k}\ndisease', v[1]))
        plt.bar([x for (x,_) in bars], [y for (_,y) in bars])
        plt.show()
