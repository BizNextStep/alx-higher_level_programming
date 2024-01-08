#!/usr/bin/python3
"""
Module for MyList class.
"""


class MyList(list):
    """
    A class that inherits from list and has a public instance method print_sorted.
    """


    def print_sorted(self):
        """
        Prints the list sorted in ascending order.
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)
    my_list.print_sorted()
    print(my_list)

