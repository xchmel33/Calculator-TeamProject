
import calc
import re

def calculation(user_input):

    #input validation
    asuffix = ")!"
    aprefix = "(log"
    operands = " +-*^/()!logr,."
    for i in range(len(user_input)):
        if user_input[i].isdigit():
            continue
        elif user_input[i] in operands:

            #ak nasleduju 2 operacie po sebe
            if i+1<len(user_input) and user_input[i+1] in operands:

                #za asuffix moze byt hoci co
                if user_input[i+1] in aprefix:
                    continue

                #pred aprefix moze byt hoci ci
                elif user_input[i] in asuffix:
                    continue

                #zaporne cisla mozu byt vsade
                elif user_input[i]=="-":
                    continue

                #inak chyba
                else:
                    raise ValueError("Invalid input")
            else:
                continue
        else:
            raise ValueError("Invalid input")

    #expression format from user_input
    expression = re.findall(r'[+\-*^/()!logr]|[0-9,.]+', user_input)

    #hidden mulitiplicaion
    i=0
    while i!=len(expression):
        if str(expression[i]).replace('.', '', 1).isdigit():

            #pred cislom je ")" alebo "!"
            if i>0 and expression[i-1] in asuffix:
                expression.insert(i,"*")
                continue

            #za cislom je "(" alebo "log"
            isafter=False
            isafter = isafter or i+1<len(expression) and expression[i+1] in aprefix

            #za cislom je dalsie cislo bez operacie
            isafter = isafter or i+1<len(expression) and str(expression[i+1]).replace('.', '', 1).isdigit()

            if isafter:
                expression.insert(i+1,"*")
            else:
                i+=1
        else:
            i+=1

    print(expression)

    #implementation
    total_parenthesis = calc.max_parenthesis(expression)

    while total_parenthesis != 0:
        expression = calc.calc_parenthesis(expression,total_parenthesis)
        total_parenthesis = calc.max_parenthesis(expression)
    else:
        expression = calc.calc_inside(expression)

    return expression



