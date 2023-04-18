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
    # print(param)
    shouldDo = True
    skip = 0
    flag = True
    param_min_size = 0
    for i in range(0, len(format_string)):
        if skip == 0:
            if format_string[i] == '#' and format_string[i+1] == '.':
                param_len = 1
                while(True):
                    if format_string[i+1+param_len].isnumeric():
                        param_min_size = param_min_size * 10 + int(format_string[i+1+param_len])
                        param_len+=1
                    elif format_string[i+1+param_len] == "k":
                        flag = True
                        break
                    else:
                        flag = False
                        shouldDo = False
                        break
                if flag == True:
                    if len(param) < param_min_size:
                        for j in range(0, len(param)):
                            if param[j].islower():
                                print(param[j].upper(), end="")
                            else:
                                print(param[j].lower(), end="")
                    else:
                        for j in range(0, param_min_size):
                            if param[j].islower():
                                print(param[j].upper(), end="")
                            else:
                                print(param[j].lower(), end="")
                    # print(param, end="")
                    skip = param_len + 1
                else:
                    print(format_string[i],end="")
            
            elif format_string[i] == '#':
                param_len = 1
                while(True):
                    if format_string[i+param_len].isnumeric():
                        param_min_size = param_min_size * 10 + int(format_string[i+param_len])
                        param_len+=1
                    elif format_string[i+param_len] == "k":
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
                    skip = param_len
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


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
