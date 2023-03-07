#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    #print(format_string)
    # print(param)
    shouldDo = True
    skip = 0
    flag = True
    param_min_size = 0
    for i in range(0, len(format_string)):
        if skip == 0:
            # if format_string[i] == '#' and format_string[i+1] == 'k':
            if format_string[i] == '#':
                k = 1
                while(True):
                    if format_string[i+k].isnumeric():
                        param_min_size = param_min_size * 10 + int(format_string[i+k])
                        k+=1
                    elif format_string[i+k] == "k":
                        flag = True
                        break
                    else:
                        flag = False
                        shouldDo = False
                        break
                if flag == True:
                    if len(param) < param_min_size:
                        for k in range(0, param_min_size - len(param)):
                            print(" ", end="")
                    for j in range(0, len(param)):
                        if param[j].islower():
                            print(param[j].upper(), end="")
                        else:
                            print(param[j].lower(), end="")
                    # print(param, end="")
                    skip = k
                else:
                    print(format_string[i],end="")
            else:
                if format_string[i].islower():
                    print(format_string[i].upper(), end="")
                else:
                    print(format_string[i].lower(), end="")
        else:
            skip -= 1
    print("")

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
