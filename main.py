from mixins import *


class Airtable(FieldsMixin, ReadMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


cars = Airtable()

commands = {'create': cars.create, 
            'update': cars.update, 
            'list': cars.list, 
            'retrive': cars.retrive, 
            'update': cars.update, 
            'delete': cars.delete,
            'len': cars.lenght
            }
while True:
    command = input('Enter command or help: ').lower()
    if command == 'help':
        print('''
              create - create car
              update - update car by id
              list - list of cars
              list(num_of_records) - list of cars last <nums_of_records>
              delete - delete car
              help - list of commands
              lenght - lenght of table
              ''')
    if command in commands:
        if command in ['create', 'len']:
            commands[command]()
        if command in 'list':
            print(commands[command](input('Enter number of rows or leave blanc to: ')))
        if command in ['delete', 'update']:
            commands[command](input('Enter id: '))
        if command in 'retrive':
            print(commands[command](input('Enter id: ')))