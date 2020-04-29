"""This module contains all functions required for the calculator
"""
import math

def isfloat(element):
    """Function determines if the input string contains a float number

    :param element: input from other functions
    :type element: string
    :return: true if input contains a float number, false if it doesn't
    """

    element = str(element).replace('.', '', 1)
    element = str(element).replace('-', '', 1)

    if element.isdigit():
        return True
    else:
        return False

def addition(expression):
    """Function calculates all additions in the expression,
    replaces operation with result and deletes operands

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :return: updated list where all additions were calculated
    """

    if expression[0]=='+':
        del expression[0]

    i = 1
    while i!=len(expression):

        if expression[i] == "+":

            expression[i]=round(float(expression[i-1])+float(expression[i+1]),10)
            expression.remove(expression[i-1])
            expression.remove(expression[i])

        else:
            i+=1

    return expression

def subtraction(expression):
    """Function firstly finds negative numbers in expression,
    deletes operation, makes the number negative and in case
    there is a number before the operation inserts '+'
    before negative number so it can be later calculated in the addition function

    :param expression: input, negative numbers are found first
    :type expression: list
    :param i: index
    :return: updated list where all negative numbers are found and subtractions replaced with additions
    """

    i=1
    while i!=len(expression):

        if isfloat(expression[i]) and expression[i-1]=="-":
            expression[i]=-float(expression[i])
            del expression[i-1]

            if i>1 and isfloat(expression[i-2]):
                expression.insert(i-1, "+")

        else:
            i+=1

    return expression

def multiplication(expression):
    """Function calculates all multiplications in the expression,
    replaces operation with result and deletes operands

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :return: updated list where all multiplications were calculated
    """

    i = 1
    while i!=len(expression):

        if expression[i] == "*":

            expression[i]=round(float(expression[i-1])*float(expression[i+1]),10)
            del expression[i-1]
            del expression[i]

        else:
            i+=1

    return expression

def division(expression):
    """Function calculates all divisions in the expression,
    replaces operation with result and deletes operands

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :raises ValueError: cannot divide by zero
    :return: updated list where all divisions were calculated
    """

    i = 1
    while i!=len(expression):

        if expression[i] == "/":

            if float(expression[i+1]) == 0:
                raise ValueError("Division by zero")

            expression[i]=round(float(expression[i-1])/float(expression[i+1]),10)
            del expression[i-1]
            del expression[i]

        else:
            i+=1

    return expression

def factorial(expression):
    """Function calculates all factorials in the expression,
    replaces operand with result and deletes operation

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :param fact: gradually updated calculation of factorial
    :type fact: int
    :raises ValueError: factorial can be calculated only for natural numbers
    :return: updated list where all factorials were calculated
    """

    i = 1
    while i!=len(expression):

        if expression[i] == "!":

            if not str(expression[i-1]).isdigit():
                raise ValueError("Factorial must be only for integers greater or equal to 0")

            fact = 1
            for k in range(1,int(expression[i-1])+1):
                fact = fact * k
            expression[i-1]=fact
            del expression[i]

        else:
            i+=1

    return expression

def power(expression):
    """Function calculates all powers in the expression,
    replaces operation with result and deletes operands

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :raises ValueError: exponent cannot be negative
    :return: updated list where all powers were calculated
    """

    i = 1
    while i!=len(expression):
        if expression[i] == "^":

            if float(expression[i+1])<0:
                raise ValueError("Exponent has to be greater or equal to 0")

            expression[i]=round(float(expression[i-1])**float(expression[i+1]),10)
            del expression[i-1]
            del expression[i]

        else:
            i+=1

    return expression

def root(expression):
    """Function calculates all roots in the expression,
    (root without argument before operation is considered as square root,
    root from negative numbers is separated)
    replaces operation with result and deletes operands

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :param x: radicand
    :type x: float
    :param n: degree
    :type n: float
    :raises ValueError: root degree cannot be negative, pair root degrees must have positive radicands
    :return: updated list where all roots were calculated
    """

    i = 0
    while i!=len(expression):
        if expression[i] == "r":

            if i>0 and isfloat(expression[i-1]):
                n=float(expression[i-1])
                x=float(expression[i+1])

            else:
                n=2
                x=float(expression[i+1])
                expression.insert(i+1,0)
                i+=1

            negative = False
            if x<0 and n%2==1:
                negative = True
                x=-x

            if x<0 and n%2==0:
                raise ValueError("Roots with pair degrees can be only calculated from positive radicands")
            if n<0:
                raise ValueError("Root degree has to be integer greater or equal to 0")

            expression[i]=x**(1/n)

            if negative:
                expression[i]=-expression[i]

            del expression[i-1]
            del expression[i]

        else:
            i+=1

    return expression

def logarithm(expression):
    """Function calculates all common logarithms in the expression
    replaces operation with result, deletes operand and other unwanted strings

    :param expression: input, so far calculated expression from other functions
    :type expression: list
    :param i: index
    :raises ValueError: cannot make logarithm with negative antilogarithm argument
    :return: updated list where all logarithms were calculated
    """

    i = 0
    while i!=len(expression):

        if expression[i] == "l" and expression[i+1] == "o" and expression[i+2]=="g":

            if float(expression[i+3]) <= 0:
                raise ValueError("Logarithm antilogarithm argument has to be greater than 0")

            expression[i]=math.log(float(expression[i+3]),10)
            del expression[i+3]
            del expression[i+2]
            del expression[i+1]

        else:
            i+=1

    return expression

def max_parenthesis(expr):
    """Function searches the expression for parenthesis
    
    :param expr: input expression
    :type expr: list
    :param opened: opened parenthesis counter
    :type opened: int
    :param max: maximum opened parenthesis counter
    :return: number of most opened parenthesis
    """

    opened = 0
    max = 0
    for i in range(len(expr)):
        if expr[i]=="(":
           opened+=1
        if expr[i]==")":
           opened-=1
        if opened > max:
           max=opened

        if opened<0:
           raise ValueError("Wrong parenthesis")
    return max

def calc_parenthesis(expr,tph):
    """Function calculates the inside of deepest parenthesis

    :param expr: input expression
    :type expr: list
    :param tph: maximum number of parenthesis in expression
    :type tph: int
    :return: updated expression with result from the deepest parenthesis
    """

    opened = closed = i  = 0
    new_elements = []

    while i != len(expr):
        if expr[i]=="(":
            opened+=1
            closed-=1
        if expr[i]==")":
            opened-=1
            closed+=1
        diff=opened-closed
        diff/=2

        if diff == tph:

            if expr[i]=="(" and expr[i+2]==")":
                del expr[i+2]
                del expr[i]
                break

            if expr[i]=="(":
                del expr[i]

            elif expr[i+1]==")":

                del expr[i+1]
                new_elements.append(expr[i])
                del expr[i]
                x=calc_inside(new_elements)
                expr.insert(i,x)
                break;

            new_elements.append(expr[i])
            del expr[i]

        else:
            i+=1

    return expr

def calc_inside(expression):
    """Function by calling other functions in mathematical order
    updates expression until the result is one number

    :param expression: input expression to be updated
    :type expression: list
    :return: result from all functions
    """
    
    result = expression
    while len(expression)!=1:

        result = factorial(result)
        result = subtraction(result)
        result = logarithm(result)
        result = root(result)
        result = power(result)
        result = multiplication(result)
        result = division(result)
        result = addition(result)

    else:
        return result[0]
