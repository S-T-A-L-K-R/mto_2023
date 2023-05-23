#!/usr/bin/env python3

import sys

table_one = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
table_two = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def modify_number(a, size):
    a = str(a)
    dot = a.find(".")
    a = a[0:i+size]
    
    retval = ''
    for i in range(0, dot):
        retval += table_two[table_one.index(i, 0)]
        pass
    
    for i in range(dot, len(a)):
        retval += str((int(a[i]) + 5) % 10)
        pass
    
    return float(retval)
    
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
                param_len = 2
                while(True):
                    if format_string[i+param_len].isnumeric():
                        param_min_size = param_min_size * 10 + int(format_string[i+param_len])
                        param_len+=1
                    elif format_string[i+param_len] == "g":
                        flag = True
                        break
                    else:
                        flag = False
                        shouldDo = False
                        break
                if flag == True and param_min_size != 0:
                    if len(param) < param_min_size:
                        for k in range(0, param_min_size - len(param)):
                            print("1", end="")
                    for j in range(0, len(param)):
                        print(modify_number(param[j], size), end="")
                    # print(param, end="")
                    skip = param_len
                else:
                    print(format_string[i], end="")
            else:
                print(format_string[i], end="")
        else:
            skip -= 1
    print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
