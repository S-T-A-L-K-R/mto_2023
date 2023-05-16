#!/usr/bin/env python3

import sys
table_one = ['a', 'b', 'c', 'd', 'e', 'f']
table_two = ['g', 'h', 'i', 'j', 'k', 'l']

def modify_param(param):
    retval = ''
    param = str(hex(int(param)))[2:]
    for x in param:
        if x in table_one:
            retval += table_two[table_one.index(x, 0)]
        else:
            retval += x
    return retval

def my_printf(format_string, param):
    #print(format_string)
    shouldDo = True
    for i in range(0, len(format_string)):
        if shouldDo:
            if format_string[i] == '#' and format_string[i+1] == 'j':
                param = modify_param(param)
                print(param, end="")
                shouldDo = False
            else:
                print(format_string[i],end="")
        else:
            shouldDo = True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
