#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    index = 0
    while count < x:
        try:
            if isinstance(my_list[index], int):
                print("{:d}".format(my_list[index]), end=" ")
                count += 1
        except IndexError:
            break
        finally:
            index += 1
    print()
    return count
