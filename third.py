import random
import unittest


def create_file():
    f = open('new.txt', 'w')
    new_len = int(input('Введите длину файла: '))
    for i in range(new_len):
        f.write(str(random.randint(0, 1000)) + '\n')
    f.close()
    return new_len


def read_lines(new_len):
    f = open('new.txt', 'r')
    read_len = int(input('Введите количество строчек: '))
    if read_len < new_len:
        lines = [line.strip() for line in f]
        required = lines[new_len - read_len:]
        print(required)
    else:
        print('Слишком мало строчек')


first = create_file()
read_lines(first)
