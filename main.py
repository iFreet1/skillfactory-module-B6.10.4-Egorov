from guest import Guest, Mentor

persons = [Guest(name='Иванов', city='г. Москва'),
           Mentor(name='Петров', city='г. Химки')]

for person in persons:
    person.show_information()