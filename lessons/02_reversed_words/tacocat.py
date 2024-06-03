import sys


def my_reversed(string):
    reversed_string = []
    x = len(string)
    for _ in range(len(string)):
        reversed_string.append(string[x-1])
        x = x - 1
    return reversed_string


while True:
    string = input()
    print(''.join(list(my_reversed(string))))
      
