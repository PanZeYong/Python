filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('Welcome to the python world!\n');
    file_object.write('Welcome to the javascript world!\n');

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n');
    file_object.write('I love createing apps that can run in a browser.\n');