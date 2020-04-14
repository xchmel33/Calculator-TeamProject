######################
# IVS - team project #
#     Calculator     #
######################
#       Authors:     #
# xchmel33, xhurba03 #
######################

import calc
import re

def main(user_input)

    #errors check
    operands = " +\-*^/()!logr"
    for i in range(len(user_input)):
        if user_input[i].isdigit():
            continue
        elif user_input[i] in operands:
            continue
        else:
            raise ValueError("Invalid input")

    elements = re.findall(r'[+\-*^/()!logr]|[0-9,.]+', user_input)

    #implementation
    total_parenthesis = calc.max_parenthesis(elements)

    while total_parenthesis != 0:
        elements = calc.calc_parenthesis(elements,total_parenthesis)
        total_parenthesis = calc.max_parenthesis(elements)
    else:
        elements = calc.calc_inside(elements)

    return elements
