# SL_data
very basic library to save and load data from a file.

This is a simple data management library for loading, saving and managing data.

I'm new to python (6 months) and I am still learning so if there's any problems or stuff that can be optimized feel free to coment

The usage is simple, here's some example python code:

    import SL_data as sl

    values = sl.SL('saved.txt')

    values.save('int_value', 42)
    values.save('some_string', 'Lorem ipsum')
    values.save('tuple', (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5))

the code above saves data to a specified name
if there is some data in file with the same name, the data will be overwritten
if there is no data of specified name the library will add a new line and save values there

    print(values.load('int_value'))
    print(values.load('some_string'))
    print(values.load('tuple'))

**output:**

    42
    Lorem ipsum
    ('3', ' 1', ' 4', ' 1', ' 5', ' 9', ' 2', ' 6', ' 5', ' 3', ' 5')

The code is still under construction so
for now everything loaded is loaded as strings
of characters but i'm working on improving this

    values.remove_data('some_string')

this will remove 'some_string' from saved file

    values.erase()

this will erase all contents of the file
However it will ask whether to delete all data for sure
this can be sped up by passing True as an argument

the message is for safety reasons only and from my experience
this was very helpful (mistakes happen)


the file with saved values looks for example like this:

    int_value:42
    some_string:Lorem ipsum
    tuple:(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)


