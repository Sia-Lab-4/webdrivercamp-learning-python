#!/usr/bin/python3

def tuple_return(argument):
    if len(argument) == 0:
        return (0, None)
    else:
        return(len(argument), argument[0])

