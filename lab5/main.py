#!/usr/bin/env python3

import sys

def modify_param(param):
    retval = ''
    for x in param:
        a = int(x)
        if a <= 0:
            a = 10
        a -= 1
        retval += str(a)
    return retval

def my_printf(format_string, param):
    #print(format_string)
    shouldDo = True
    g_index = 0
    for i in range(0, len(format_string)):
        if shouldDo and i >= g_index:
            # if format_string[i] == '#' and format_string[i+1] == 'g':
            if format_string[i] == '#':
                g = format_string.find("g", i)
                if g > (i + 1):
                    x = format_string[i+1 : g]
                    if x.isdigit():
                        x = int(x)
                        param = modify_param(param)
                        if x > len(param):
                            print(" " * (x - len(param)), end="")
                        g_index = g + 1
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
