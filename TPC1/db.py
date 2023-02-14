class person:
    def __init__(self, line: str):
        raw = line.split(',')
        self.data_fields = {}
        self.data_fields['age'] = int(raw[0])
        self.data_fields['sex'] = raw[1]
        self.data_fields['tension'] = int(raw[2])
        self.data_fields['colesterol'] = int(raw[3])
        self.data_fields['heart_bpm'] = int(raw[4])
        self.data_fields['has_disease'] = raw[5][1] == '1'

class db:
    def __init__(self, content: list[str]):
        self.db_content = []
        self.db_table: dict = {}

        for line in content:
            self.db_content.append(person(line))

    def __eq__(self, other: object) -> bool:
        return self.db_content == other.content
