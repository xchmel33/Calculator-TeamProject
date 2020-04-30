######################
# IVS - team project #
#     Calculator     #
######################

import fileinput
import calc

#get all items from stdin
def getAllItems():
    allItems = []
    for item in fileinput.input():
        allItems.append(float(item))
    return allItems

#calculating arithmetic mean from input data
def arithmeticMean(allItems):
    arithmeticMean = []
    for item in allItems:
        arithmeticMean.append(item)
        arithmeticMean.append('+')
    arithmeticMean.pop()
    sum = calc.addition(arithmeticMean)
    n = len(allItems)
    array = [sum[0], "/", n]
    return calc.division(array)

#function returns standard error of mean
def deviation(allItems, arithmeticMean):
    result = [0]
    for i in allItems:
        part = calc.subtraction([i, "-", arithmeticMean])
        part = calc.addition(part)[0]
        part = calc.power([part, "^", 2])
        result = calc.addition([result[0], "+", part[0]])

    deviation = calc.division([result[0], "/", calc.addition([len(allItems), "+", -1])[0]])[0]
    deviation = calc.root(["r", deviation])[0]
    return deviation

allItems = getAllItems()
arithmeticMean = arithmeticMean(allItems)[0]
result = deviation(allItems, arithmeticMean)
print(result)
