#!/usr/bin/env python3

def famous_births(inp_dict):
    temp_list = []

    for i in inp_dict:
        temp_list.append(inp_dict[i])
    
    for i in range(len(temp_list) - 1):
        swapped = False
        for j in range(len(temp_list) - i - 1):
            if int(temp_list[j]['date_of_birth']) > int(temp_list[j+1]['date_of_birth']):
                temp_list[j], temp_list[j+1] = temp_list[j+1], temp_list[j]
                swapped = True
        if not swapped:
            break

    for i in temp_list:
        print(f'{i['name']} is a great scientist born in {i['date_of_birth']}.')

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)