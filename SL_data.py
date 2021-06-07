"""
made by *Lirgo*

***SL_data***

very basic library to save and load data from a file
version 0.2
"""
import os

lib_name = 'SL_data'
lib_version = 0.2
lib_description = 'very basic library to save and load data from a file'

print(f'Thanks for using {lib_name} library')
print(f'version {lib_version}')

class data_name_not_found(Exception):
    pass
class SL:
    def __init__(self, path, welcome=True):
        self.path = path

    def save(self, name, data):
        file = open(self.path, 'r')
        buffer = open('buffer', 'w')

        try:
            _ = data[0]
            data = tuple(data)
        except TypeError:
            _ = None

        skipped = False
        for line in file:
            skip = False
            data_name = ""
            for ch in line:
                if ch == ':':
                    if data_name == name:
                        skip = True
                        skipped = True
                        buffer.write(name + ':' + str(data) + '\n')
                    else:
                        break
                data_name += ch
            if not skip:
                buffer.write(line)

        buffer.close()
        file.close()

        if skipped:
            file = open(self.path, 'w')
            buffer = open('buffer', 'r')

            for line in buffer:
                file.write(line)

            buffer.close()
            file.close()
        else:
            file = open(self.path, 'a')
            file.write(name + ':' + str(data) + '\n')
        os.remove('buffer')

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
        file = open(self.path, 'r')
        found = False
        for line in file:
            data_name = ''
            for ch in line:
                if not found:
                    if ch == ':':
                        if data_name == name:
                            found = True
                            data_name = ''
                        else:
                            break
                data_name += ch
            if found:
                ret = data_name[1:]
                if ret[0] == '(':
                    new_ret = []
                    one_val = ''
                    for char in ret[1:]:
                        if char == ')':
                            new_ret.append(one_val)
                            return tuple(new_ret)
                        elif char == ',':
                            new_ret.append(one_val)
                            one_val = ''
                        else:
                            one_val += char
                else:
                    return ret
        if not found:
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


