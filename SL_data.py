"""
made by *Lirgo*

***SL_data***

very basic library to save and load data from a file
version 0.3.0
"""
import os

lib_name = 'SL_data'
lib_version = '0.3.0'
lib_description = 'very basic library to save and load data from a file'

print(f'Thanks for using {lib_name} library')
print(f'version {lib_version}')
print()

class data_name_not_found(Exception):
    pass
class SL:
    def __init__(self, path, welcome=True):
        self.path = path
        self.data_types = []
        self.data_names = []
        self.data_values = []
        self.update_arrays()

    def update_arrays(self):
        self.data_types = []
        self.data_names = []
        self.data_values = []
        file = open(self.path, 'r')
        for line in file:
            data_name = ''
            data_type = ''
            for index, ch in enumerate(line):
                if ch == ':' and len(self.data_types) > len(self.data_names):
                    self.data_names.append(data_name)
                    self.data_values.append(line[index + 1:-1])
                    break
                elif len(self.data_types) > len(self.data_names):
                    data_name += ch
                elif ch == ':':
                    self.data_types.append(data_type)
                else:
                    data_type += ch
        file.close()

    def save(self, name, data):

        with open('buffer', 'w') as buffer:
            skipped = False
            for data_type, data_name, data_value in zip(self.data_types, self.data_names, self.data_values):
                if data_name == name:
                    buffer.write(str(type(data))[8:-2] + f':{name}:{data}\n')
                    skipped = True
                else:
                    buffer.write(f'{data_type}:{data_name}:{str(data_value)}\n')

        if skipped:
            with open(self.path, 'w') as file:
                with open('buffer', 'r') as buffer:
                    for line in buffer:
                        file.write(line)
        else:
            with open(self.path, 'a') as file:
                file.write(str(type(data))[8:-2] + f':{name}:{data}\n')
        os.remove('buffer')
        self.update_arrays()

    def remove_data(self, name):
        file = open(self.path, 'r')
        buffer = open('buffer', 'w')
        skipped = False
        for line in file:
            skip = False
            data_name = ""
            for ch in line:
                if ch == ':':
                    if data_name == name:
                        skip = True
                        skipped = True
                        break
                    else:
                        break
                data_name += ch
            if not skip:
                buffer.write(line)
        buffer.close()
        file.close()
        if not skipped:
            os.remove('buffer')
            raise data_name_not_found('could not find data of specified name')

        file = open(self.path, 'w')
        buffer = open('buffer', 'r')

        for line in buffer:
            file.write(line)

        buffer.close()
        file.close()
        os.remove('buffer')

    def load(self, name):
        for file_name, file_value in zip(self.data_names, self.data_values):
            if file_name == name:
                return file_value
        raise data_name_not_found('could not find data of specified name')

    def erase(self, confirmation=False):
        if confirmation:
            file = open(self.path, 'w')
            file.close()
            return
        else:
            answer = input('Are you sure to erase all data from ' + self.path + ' file? (Y/N)\n')
            if answer == 'Y':
                file = open(self.path, 'w')
                file.close()
            elif answer != 'N':
                print('Did not understand')
                self.erase()


