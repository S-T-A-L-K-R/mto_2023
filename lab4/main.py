#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    #print(format_string)
    shouldDo = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[i] == '#' and format_string[i+1] == 'g':
                param = str(param)[::-1]
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
