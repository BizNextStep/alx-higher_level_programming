#!/usr/bin/python3


""" Returns a list of available attributes and methods """


def lookup(obj):
    """ Look for all attributes and methods of obj """
    return [method for method in dir(obj)]
