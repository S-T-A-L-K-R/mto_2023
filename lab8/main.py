#!/usr/bin/env python3

import sys
table_one = ['a', 'b', 'c', 'd', 'e', 'f', '0']
table_two = ['g', 'h', 'i', 'j', 'k', 'l', 'o']

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
    j_index = 0
    for i in range(0, len(format_string)):
        if shouldDo and i >= j_index:
            if format_string[i] == '#':
                j = format_string.find("j", i)
                if j > (i + 1):
                    x = format_string[i+1 : j]
                    if x.isdigit():
                        x = int(x)
                        param = modify_param(param)
                        if x > len(param):
                            print(" " * (x - len(param)), end="")
                        j_index = j + 1
                        print(param, end="")
                        shouldDo = False
                    else:
                        print(format_string[i],end="")
                else:
                    print(format_string[i],end="")
            else:
                print(format_string[i],end="")
        else:
            shouldDo = True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
