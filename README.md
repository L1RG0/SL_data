# SL_data
very basic library to save and load data from a file.

This is a simple data management library for loading, saving and managing data.

I'm new to python (6 months) and I am still learning so if there's any problems or stuff that can be optimized feel free to coment

The usage is simple, here's some example python code:

    import SL_data as sl

    values = sl.SL('saved.txt')

    values.save('val_int', 42)
    values.save('val_str', 'Lorem ipsum')
    values.save('val_tup', (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5))
    values.save('val_lis', [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    values.save('val_set', {1, 121, 1331, 14641, 15101051})
    values.save('val_flt', 2.72)
    values.save('val_boo', True)
    values.save('val_com', 1 + 3j)

the code above saves data to a specified name (custom) with parsed type (currently supports only types mentioned above, if you'd like to add a new data type feel free to contact me)
if there is some data in file with the same name, the data will be overwritten
if there is no data of specified name the library will add a new line and save values there
    
    print(values.load('val_int'))
    print(values.load('val_str'))
    print(values.load('val_tup'))
    print(values.load('val_lis'))
    print(values.load('val_set'))
    print(values.load('val_flt'))
    print(values.load('val_boo'))
    print(values.load('val_com'))

**output:**

    42
    Lorem ipsum
    ('3', '1', '4', '1', '5', '9', '2', '6', '5', '3')
    ['1', '1', '2', '3', '5', '8', '13', '21', '34']
    {'14641', '1', '1331', '121'}
    2.72
    True
    (1+3j)

The code is still under construction so
for now lists, tuples and sets are loaded with strings inside but i'm working on improving this

    values.remove_data('data_name')

this will remove 'data_name' from a saved file

    values.erase()

this will erase all contents of the file
However it will ask whether to delete all data for sure.

This can be sped up by passing True as an argument

The message is for safety reasons only and from my experience
this was very helpful (mistakes happen)


The file with saved values from the examples above looks like this:

    int:val_int:42
    str:val_str:Lorem ipsum
    tuple:val_tup:(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
    list:val_lis:[1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    set:val_set:{1, 14641, 1331, 121, 15101051}
    float:val_flt:2.72
    bool:val_boo:True
    complex:val_com:(1+3j)



