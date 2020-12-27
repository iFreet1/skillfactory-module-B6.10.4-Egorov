class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def get_person_data(self):
        return f'{self.name}, {self.city}'


class Guest(Person):
    STATUS = '"Гость"'

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def show_information(self):
        print(f'{self.get_person_data()}, статус {self.STATUS}')


class Mentor(Person):
    STATUS = '"Наставник"'

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def show_information(self):
        print(f'{self.get_person_data()}, статус {self.STATUS}')