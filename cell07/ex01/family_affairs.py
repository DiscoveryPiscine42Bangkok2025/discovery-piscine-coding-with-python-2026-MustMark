#!/usr/bin/env python3

def find_the_redheads(inp_dict):
    temp = []

    for i in inp_dict:
        if inp_dict[i] == 'red':
            temp.append(i)

    return temp

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))
