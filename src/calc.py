######################
# IVS - team project #
#     Calculator     #
######################
#       Authors:     #
# xchmel33, xhurba03 #
######################

#import main.py
#import calc.py

import re
import math

#calc.py:

#function operates all additons in expression(string)
def addition(expression):

    if expression[0]=='+':
        del expression[0]

    i = 1
    while i!=len(expression):

        #find operation
        if expression[i] == "+":

            #convert string to float
            x=float(expression[i-1])
            y=float(expression[i+1])

            #additon
            expression[i]=round(x+y,10)

            #remove solved parts of string in expression
            expression.remove(expression[i-1])
            expression.remove(expression[i])

        else:
            i+=1

    #return updated expression(string) with results from addition
    return expression

#function finds negative numbers and replaces subtraction
#with addition of opposite number in expression(string)
def subtraction(expression):

    i=1
    while i!=len(expression):

        #find negative number
        if str(expression[i]).replace('.', '', 1).isdigit() and expression[i-1]=="-":
            expression[i]=-float(expression[i])
            del expression[i-1]

            #in case of subtraction
            if i>1 and str(expression[i-2]).replace('.', '', 1).isdigit():
                expression.insert(i-1, "+")

        else:
            i+=1

    #return updated array expression with negative numbers
    return expression

#function operates all multiplications in array expression
def multiplication(expression):

    i = 1
    while i!=len(expression):

        #find operation
        if expression[i] == "*":

            #convert string to float
            x=float(expression[i-1])
            y=float(expression[i+1])

            #multiplication
            expression[i]=round(x*y,10)

            #remove solved parts of string in expression
            del expression[i-1]
            del expression[i]

        else:
            i+=1

    #return updated array expression with results from multiplication
    return expression

#function operates all divisions in array expression
def division(expression):

    i = 1
    while i!=len(expression):

        #find operation
        if expression[i] == "/":

            #convert string to float
            x=float(expression[i-1])
            y=float(expression[i+1])

            #error check
            if y == 0:
                raise ValueError("Division by zero")

            #division
            expression[i]=round(x/y,10)


            #remove solved parts of string in expression
            expression.remove(expression[i-1])
            expression.remove(expression[i])

        else:
            i+=1

    #return updated array expression with results from division
    return expression

#function operates all factiorials in array expression
def factorial(expression):

    i = 1
    while i!=len(expression):

        #find operation
        if expression[i] == "!":

            #convert string to float
            x=int(expression[i-1])

            #error check
            if x<0:
                raise ValueError("Factorial must be only for numbers greater or equal to 0")

            #factiorial
            fact = 1
            for k in range(1,x+1):
                fact = fact * k
            expression[i-1]=fact

            #remove solved parts of string in array expression
            del expression[i]

        else:
            i+=1

    #return updated array expression with results from factorial
    return expression

#function operates all powers in array expression
def power(expression):

    i = 1
    while i!=len(expression):
        if expression[i] == "^":

            #convert string to float
            x=float(expression[i-1])
            n=float(expression[i+1])

            #error check
            #if x<0:
            #    raise ValueError("Exponent has to be integer, which is greater or equal 0")

            #power calculation
            expression[i]=round(x**n,10)

            #remove solved parts of string in array expression
            del expression[i-1]
            del expression[i]

        else:
            i+=1

    #return updated array expression with results from power
    return expression

#function operates all roots in array expression
def root(expression):

    i = 0
    while i!=len(expression):
        if expression[i] == "r":

            #root with both arguments
            if i>0 and str(expression[i-1]).replace('.', '', 1).isdigit():
                n=float(expression[i-1])
                x=float(expression[i+1])

            #defalut root:
            else:
                n=2
                x=float(expression[i+1])
                
                #array maintenance
                expression.insert(i+1,0)
                i+=1

            #negative root
            negative = False
            if x<0 and n%2==1:
                negative = True
                x=-x


            #error check
            if x<0 and n%2==0:
                raise ValueError("Sqaure roots can be only from possitive numbers")
            if n<0:
                raise ValueError("Root has to be integer or equal to 0")

            #root calculation
            expression[i]=x**(1/n)
            if negative:
                expression[i]=-expression[i]

            #remove solved parts of string in array expression
            del expression[i-1]
            del expression[i]

        else:
            i+=1

    #return updated array expression with results from root
    return expression

#+lub funkce
#function operates all logartims in array expression
def logarithm(expression):

    i = 0
    while i!=len(expression):

        #find operation
        if expression[i] == "l" and expression[i+1] == "o" and expression[i+2]=="g":

            if str(expression[i+3]).replace('.', '', 1).isdigit():
                a=10
                x=float(expression[i+3])

            #error check
            if x <= 0:
                raise ValueError("Logarithm x argument has to be greater than 0")

            #log calculation
            expression[i]=round(math.log(x,a))

            #remove solved parts of string in array expression
            if i+4 != len(expression) and str(expression[i+4]).replace('.', '', 1).isdigit():
                del expression[i+4]
            del expression[i+3]
            del expression[i+2]
            del expression[i+1]

        else:
            i+=1

    #return updated array expression with results from logaritm
    return expression

#function calculates the number of opened parenthesis in given array
def max_parenthesis(expr):

   opened = 0
   max = 0
   for i in range(len(expr)):
       if expr[i]=="(":
           opened+=1
       if expr[i]==")":
           opened-=1
       if opened > max:
           max=opened

   #return the number of most opened parenhesis
   return max

#function calculates the inside of deepest parenthesis
def calc_parenthesis(expr,tph):

    opened = closed = i  = 0
    new_elements = []

    #errors check
    if expr[0]==")":
        raise ValueError("Wrong start parenthesis )")

    #
    while i != len(expr):
        if expr[i]=="(":
            opened+=1
            closed-=1
        if expr[i]==")":
            opened-=1
            closed+=1
        diff=opened-closed
        diff/=2

        #inside deepest parenthesis
        if diff == tph:

            #single num inside
            if expr[i]=="(" and expr[i+2]==")":
                del expr[i+2]
                del expr[i]
                break

            #delete start parenthesis
            if expr[i]=="(":
                del expr[i]

            #at the end
            elif expr[i+1]==")":

                #delete parenthesis
                del expr[i+1]

                #save to new array and delete old
                new_elements.append(expr[i])
                del expr[i]

                #get result of inside parethesis
                x=calc_inside(new_elements)
                expr.insert(i,x)
                break;

            #save to new array and delete old
            new_elements.append(expr[i])
            del expr[i]

        else:
            i+=1

    #return updated array without deepest parenthesis
    return expr

def calc_inside(expression):

    #factorial
    result = factorial(expression)
    print("result after factorial="+str(result))

    #change subtraction to negative
    result = subtraction(result)
    print("result after negative="+str(result))

    #logaritm
    result = logarithm(result)
    print("result after log="+str(result))

    #root
    result = root(result)
    print("result after root="+str(result))

    #power
    result = power(result)
    print("result after power="+str(result))

    #multiply
    result = multiplication(result)
    print("result after mul="+str(result))

    #division
    result = division(result)
    print("result after div="+str(result))

    #addition
    result=addition(result)
    print("result after add="+str(result))

    return result[0]

def sqrt(number):
    return math.sqrt(number)
