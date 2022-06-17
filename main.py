from mixins import *


class Airtable(FieldsMixin, ReadMixin, CreateMixin, UpdateMixin, DeleteMixin):
    pass


cars = Airtable()
commands = {'create': cars.create, 
            'update': cars.update, 
            'list': cars.list,
            'retrieve': cars.retrieve,
            'delete': cars.delete,
            'length': cars.length
            }
while True:
    command = input('Enter command or help: ').lower()
    if command == 'help':
        print('''
              create - create car
              update - update car by id
              list - list of cars
              retrieve - car by id
              list(num_of_records) - list of cars last <nums_of_records>
              delete - delete car
              help - list of commands
              length - length of table
              ''')
    if command in commands:
        if command in ['create', 'length']:
            commands[command]()
        elif command in 'list':
            print(commands[command](input('Enter number of rows or leave blanc to: ')))
        elif command in ['delete', 'update']:
            cars.list_of_id()
            commands[command](input('Enter id: '))
        elif command in 'retrieve':
            cars.list_of_id()
            print(commands[command](input('Enter id: ')))
        else:
            print('unknown command')
