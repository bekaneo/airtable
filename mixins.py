import json
import requests
from settings import settings


class FieldsMixin:
    car_types = ['sedan', 'hatchback', 'univarsal',
                 'coupe', 'minivan', 'suv', 'pickup']

    def check_id(self, id_):
        data = requests.get(f'{settings.get_url}/{id_}',
                            headers=settings.HEADERS).json()
        return True if data.get('error') != 'NOT_FOUND' else False

    def lenght(self):

        data = self.list()
        print(f'Numbers of rows in table: {len(data["records"])}')

    @property
    def fields(self):
        fields = self.list(1)
        records = fields['records'][0]['fields']
        fields = list(records)
        return fields

    def validate(self, id_=None):
        if not id_:
            print('[PROCESSING...]')
            fields = self.fields
            data = self.retrive('recxUzoQvw6VlSUfk')
            record = data['fields']
            print(f'You shoud enter these fields: {", ".join(fields)}')
            for field in fields:
                if field == 'type':
                    while True:
                        user_input = input(
                            f'Enter {field.upper()} {self.car_types}: ').lower()
                        if user_input in self.car_types and user_input != '':
                            record[field] = user_input
                            break
                        else:
                            print(
                                f'Enter valid {field.upper()} you entered {user_input}')
                if field in 'brand, model, color':
                    while True:
                        user_input = input(
                            f'Enter {field.upper()} a string: ').lower()
                        if user_input.isalpha() and user_input != '':
                            record[field] = user_input
                            break
                        else:
                            print(
                                f'Enter valid {field.upper()} you entered {user_input}')
                if field in 'volume, mileage, year, price':
                    while True:
                        user_input = input(
                            f'Enter {field.upper()} an integer: ').lower()
                        if user_input.replace('.', '').isdigit() and user_input != '':
                            record[field] = user_input
                            break
                        else:
                            print(
                                f'Enter valid {field.upper()} you entered {user_input}')
            data = {'fields': record, 'typecast': True}
            return json.dumps(data)
        else:
            print('[PROCESSING...]')
            fields = self.fields
            data = self.retrive(id_)
            record = data['fields']
            print(f'Record by id: \n {record}')
            fields_to_change = input(
                f'What fields do you want ot change: {", ".join(fields)} \
                    \nprint field by space or ENTER to change all fields: ')
            if not fields_to_change:
                fields_to_change = fields
            else:
                fields_to_change = fields_to_change.split(' ')
            for field in fields_to_change:
                if field in fields:
                    if field == 'type':
                        while True:
                            user_input = input(
                                f'Enter {field.upper()} {self.car_types}: ').lower()
                            if user_input in self.car_types and user_input != '':
                                record[field] = user_input
                                break
                            else:
                                print(
                                    f'Enter valid {field.upper()} you entered {user_input}')
                    if field in 'brand, model, color':
                        while True:
                            user_input = input(
                                f'Enter {field.upper()} a string: ').lower()
                            if user_input.isalpha() and user_input != '':
                                record[field] = user_input
                                break
                            else:
                                print(
                                    f'Enter valid {field.upper()} you entered {user_input}')
                    if field in 'volume, mileage, year, price':
                        while True:
                            user_input = input(
                                f'Enter {field.upper()} an integer: ').lower()
                            if user_input.replace('.', '').isdigit() and user_input != '':
                                record[field] = user_input
                                break
                            else:
                                print(
                                    f'Enter valid {field.upper()} you entered {user_input}')
                else:
                    print(f'{field} not found')
            data = {'fields': record, 'typecast': True}
            return json.dumps(data)


class ReadMixin:
    def list(self, records: int = None) -> str:
        max_records = '?maxRecords='
        if not records:
            print('[PROCESSING...]')
            cars = requests.get(settings.get_url, headers=settings.HEADERS)
        else:
            print('[PROCESSING...]')
            cars = requests.get(
                f'{settings.get_url}{max_records}{records}', headers=settings.HEADERS)
        return cars.json()

    def retrive(self, id_):
        print('[PROCESSING...]')
        if self.check_id(id_):
            print('[PROCESSING...]')
            car = requests.get(f'{settings.get_url}/{id_}',
                               headers=settings.HEADERS)
            return car.json()
        else:
            print(f'Not found this id')


class CreateMixin():

    def create(self):
        print('[PROCESSING...]')
        data = self.validate()
        request = requests.post(url=settings.get_url,
                                headers=settings.HEADERS, data=data)
        print('Successefully created!')
        return request.json()


class UpdateMixin:
    def update(self, id_):
        print('[PROCESSING...]')
        if self.check_id(id_):
            data = self.validate(id_)
            print('[PROCESSING...]')
            request = requests.patch(
                url=f'{settings.get_url}/{id_}', headers=settings.HEADERS, data=data)
            print('Successefully updated!')
            return request.json()
        else:
            print(f'Not found this id')


class DeleteMixin:
    def delete(self, id_):
        if self.check_id(id_):
            print('[PROCESSING...]')
            request = requests.delete(
                f'{settings.get_url}/{id_}', headers=settings.HEADERS)
            print('Successefully deleted!')
            return request.json()
        else:
            print(f'Not found this id')