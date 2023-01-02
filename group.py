class Person:
    persons = []

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.persons.append(self)

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name: str, people: Person.persons):
        self.name = name
        self.people = people
        self.start = 0
        self.end = len(self.people)

    def __len__(self):
        return len(self.people)

    def __repr__(self):
        text = []
        for pers in self.people:
            text.append(f"{pers.name} {pers.surname}")
        return f"Group {self.name} with members {', '.join(text)}"

    def __add__(self, other):
        return Group(f"{self.name} {other.name}", self.people + other.people)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            ret = f"Person {self.start}: {self.people[self.start]}"
            self.start += 1
            return ret
        else:
            raise StopIteration

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item]}"

