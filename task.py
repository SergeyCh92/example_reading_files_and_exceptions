import os
from pprint import pprint


def read_f(file_name):
    cook_book = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            cook_book[line] = []
            count = int(f.readline())
            for i in range(count):
                my_str = f.readline()
                ingredient_name, quantity, measure = my_str.split('|')
                list_foodstuff = {'ingredient_name': ingredient_name.strip(), 'quantity': quantity.strip(),
                                  'measure': measure.strip()}
                cook_book[line].append(list_foodstuff)
            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    voc_dish = read_f('cook_book.txt')
    voc_result = {}
    for i in dishes:
        for ing in voc_dish[i]:
            if ing['ingredient_name'] in voc_result:
                voc_result[ing['ingredient_name']]['quantity'] += person_count * int(ing['quantity'])
            else:
                voc_result[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': person_count *
                                                                                             int(ing['quantity'])}

    return voc_result


pprint(read_f('cook_book.txt'))
print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
