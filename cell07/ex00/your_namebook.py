#!/usr/bin/env python3

def array_of_names(inp_dict):
    temp = []

    for i in inp_dict:
        temp.append(i.capitalize() + ' ' + inp_dict[i].capitalize())
    
    return temp

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
