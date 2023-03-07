#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    #print(format_string)
    # print(param)
    shouldDo = True
    for i in range(0, len(format_string)):
        if shouldDo:
            if format_string[i] == '#' and format_string[i+1] == 'k':
                for j in range(0, len(param)):
                    if param[j].islower():
                        print(param[j].upper(), end="")
                    else:
                        print(param[j].lower(), end="")
                # print(param, end="")
                shouldDo=False
            else:
                if format_string[i].islower():
                    print(format_string[i].upper(), end="")
                else:
                    print(format_string[i].lower(), end="")
        else:
            shouldDo=True
    print("")

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
