#!/usr/bin/env python3

import sys

def modify_param(param):
    retval = ''
    for x in param:
        a = int(x)
        if a <= 0:
            a = 10
        a -= 1
        retval.append(str(a))
    return param

def my_printf(format_string, param):
    #print(format_string)
    shouldDo = True
    for i in range(0, len(format_string)):
        if shouldDo:
            # if format_string[i] == '#' and format_string[i+1] == 'g':
            if format_string[i] == '#':
                g_index = format_string.find("g", i)
                if g_index > i:
                    x = int(param[i:g_index])
                    param = modify_param(param)
                    if x > len(param):
                        print(" " * (x - len(param)))
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
