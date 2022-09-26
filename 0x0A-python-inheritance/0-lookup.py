#!/usr/bin/python3
""" module `0-lookup` contains the `lookup` function """


def lookup(obj):
    """ returns the list of of available attributes and methods for `obj` """
    return dir(obj)
