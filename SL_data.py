"""
made by *Lirgo*

***SL_data***

very basic library to save and load data from a file
version 1.0.0 alpha
"""

def change_type(data_type, value):
    if   data_type == 'int'    : return int(value)
    elif data_type == 'float'  : return float(value)
    elif data_type == 'bool'   : return value == 'True'
    elif data_type == 'str'    : return value
    elif data_type == 'complex': return complex(value)
    elif data_type in ('tuple', 'list', 'set'):
        output = []
        one_val = ''
        for ch in value:
            if ch not in ('{', '}', '(', ')', '[', ']', ' '):
                if ch == ',':
                    output.append(one_val)
                    one_val = ''
                else:
                    one_val += ch

        if data_type == 'tuple': return tuple(output)
        elif data_type == 'set': return set(output)
        else: return output

    raise data_name_error('file type not supported, please contact the library author for possible implementation')

class data_name_error(Exception):
    pass
class SL:
    def __init__(self, path):
        self.path = path
        self.data_types = []
        self.data_names = []
        self.data_values = []
        self.update_arrays()

    def reset_values(self):
        self.data_types = []
        self.data_names = []
        self.data_values = []

    def update_arrays(self):
        self.reset_values()
        with open(self.path, 'r') as file:
            for line in file:
                temp_str = ''
                for index, ch in enumerate(line):
                    if ch == ':' and len(self.data_types) > len(self.data_names):
                        self.data_names.append(temp_str)
                        self.data_values.append(line[index + 1:-1])
                        break
                    elif ch == ':':
                        self.data_types.append(temp_str)
                        temp_str = ''
                    else: temp_str += ch

    def save(self, name, data):
        if ':' in name: raise data_name_error('name cannot have any colons')
        with open(self.path, 'w') as file:
            skipped = False
            for data_type, data_name, data_value in zip(self.data_types, self.data_names, self.data_values):
                if data_name == name:
                    file.write(str(type(data))[8:-2] + f':{name}:{data}\n')
                    skipped = True
                else:
                    file.write(f'{data_type}:{data_name}:{str(data_value)}\n')

            if not skipped: file.write(str(type(data))[8:-2] + f':{name}:{data}\n')
        self.update_arrays()

    def remove_data(self, name):
        for index, data_name in enumerate(self.data_names):
            if data_name == name:
                del self.data_names[index]
                del self.data_types[index]
                del self.data_values[index]

        with open(self.path, 'w') as file:
            for data_type, data_name, data_value in zip(self.data_types, self.data_names, self.data_values):
                file.write(f'{data_type}:{data_name}:{str(data_value)}\n')

    def load(self, name):
        for file_type, file_name, file_value in zip(self.data_types, self.data_names, self.data_values):
            if file_name == name: return change_type(file_type, file_value)
        raise data_name_error('could not find data of specified name')

    def erase(self, confirmation=False):
        if confirmation:
            with open(self.path, 'w'):
                _ = 42
            self.reset_values()
        else:
            answer = input('Are you sure to erase all data from ' + self.path + ' file? (Y/N)\n')
            if answer == 'Y':
                self.erase(True)
            elif answer != 'N':
                print('Did not understand')
                self.erase()
