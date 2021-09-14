import os

current_path = os.path.dirname(__file__)
file_path = current_path + '\\test.txt'

# standard method, must close the file
""" f = open(file_path, 'r')
print(f.mode)
f.close() """

# context manager, the file is open within this block of code
# when your out of the block, the file closes
# f is still accessible outside this block, though it will remain closed
""" with open(file_path, 'r') as f:
    for line in f:
        print(line, end='') """

# f.read() reads the whole file, you can specify number of chars to read as an arg
# f.read() returns an empty string as the eof, each time it's executed it continues where it left of
# f.readlines() reads line by line, useful for large files
# f.readline() reads the next line in file

""" with open(file_path, 'r') as f:
    size_to_read = 100
    
    f_contents = f.read(size_to_read) # first characters
    
    while len(f_contents) > 0: #when eof is reached, f_contents = ''
        print(f_contents, end='')
        f_contents = f.read(size_to_read) # next characters """

# f.tell() returns the position you are at reading the file
""" with open(file_path, 'r') as f:
    size_to_read = 10
    
    f_contents = f.read(size_to_read)

    print(f.tell()) """ # your at f.tell() position o f, because just read size_to_read chars

# you can prevent the previous behaviour with f.seek() passing 0 to seek for the first char

""" with open(file_path, 'r') as f:
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    f.seek(0)
    f_contents = f.read(size_to_read) # read from the beginning
    print(f.tell()) """ # again is at 10th position

############# Writing
file_path2 = current_path + '\\test2.txt'
""" with open (file_path2, 'w') as f: # if the file exists, overwrites it, otherwise it creates the file and then writes into it
    f.write('Hello World') """

# so you can create new files like this
""" with open (file_path, 'w') as f:
    pass """

## Copy from one file to another, or append with 'a' argument in open

with open (file_path, 'r') as read_file:
    with open (file_path2, 'a') as write_file:
        for line in read_file:
            write_file.write(line)