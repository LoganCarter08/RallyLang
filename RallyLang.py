# -*- coding: utf-8 -*-
"""
Super simple implementation of rallyLang
"""
from sys import exit

class Variable:
  def __init__(self, myType, value, name):
    self.type = myType
    self.value = value
    self.name = name

def getVarValue(varName):
    for var in variables:
        if var.name == varName:
            return var.value

def getVarType(varName):
    for var in variables:
        if var.name == varName:
            return var.type

def setVarValue(varName, val):
    for var in variables:
        if var.name == varName:
            var.value = val
            return True
    return False

def isVar(string):
    try:
        if string[0] == 'L' or string[0] == 'R':
            if string[1] >= '0' and string[1] <= '6':
                return True
            else:
                return False 
        return False 
    except:
        return False

def addition(left, right, currentVarType):
    if currentVarType == 1:                                            # this is an illegal method
        return left
    elif currentVarType == 3: 
        if splitLine[i - 1].isnumeric():
            left = chr(int(left))
        if splitLine[i + 1].isnumeric():
            right = chr(int(right))
    elif currentVarType == 2:
        left = float(splitLine[i - 1])
        right = float(splitLine[i + 1])
    return (left + right)

def subtraction(left, right, currentVarType):
    if currentVarType == 3 or currentVarType == 1:                     # this is an illegal method
        return left
    elif currentVarType == 2:
        left = float(splitLine[i - 1])
        right = float(splitLine[i + 1])
    return (left - right)

def multiplication(left, right, currentVarType):
    if currentVarType == 3 or currentVarType == 1:                     # this is an illegal method
        return left
    elif currentVarType == 2:
        left = float(splitLine[i - 1])
        right = float(splitLine[i + 1])
        return (left * right)

def division(left, right, currentVarType):
    if currentVarType == 3 or currentVarType == 1:                     # this is an illegal method
        return left
    elif currentVarType == 2:
        left = float(splitLine[i - 1])
        right = float(splitLine[i + 1])
        return (left / right)

variables = []

fileName = ""
f = open("Test Files/SimpleIntegerMath.txt", "r")
#f = open("Test Files/HelloWorld.txt", "r")

Lines = f.read()
Lines = Lines.replace("\t", "\n") # new line is acceptable separator and so is tab, so combine them
Lines = Lines.split("\n") # split the input into the commands

for line in Lines:
    splitLine = line.split(" ")
    ###### line preprocess ############
    currentVarType = 0 # 1 = bool, 2 = double, 3 = string
    leftOfInto = True
    runOperations = True
    i = 0
    while i < len(splitLine):
        if "finish" == splitLine[i]:
            exit(0)
        elif "slpy" in splitLine[i]:   
            variables.append(Variable(3, "", splitLine[i + 1]))
            splitLine.pop(i)
            currentVarType = 3
            i = i - 1
        elif "lg" in splitLine[i]:
            variables.append(Variable(2, "", splitLine[i + 1]))
            splitLine.pop(i)
            currentVarType = 2
            i = i - 1
        elif "sh" in splitLine[i]:
            variables.append(Variable(1, "", splitLine[i + 1]))
            splitLine.pop(i)
            currentVarType = 1
            i = i - 1
        # not within operations as this is too simplistic to need a real parse
        elif "unseen" in splitLine[i]:                          
            runOperations = False
            setVarValue(splitLine[i + 1], getVarValue(splitLine[i + 1]) * -1)
        elif i > 0 and "->" in splitLine[i - 1]:
            if isVar(splitLine[i]):
                currentVarType = getVarType(splitLine[i])
            leftOfInto = False
        elif i > 0 and isVar(splitLine[i - 1]):
            if leftOfInto:
                splitLine[i - 1] = getVarValue(splitLine[i - 1])
        elif "cut" in splitLine[i]:
            runOperations = False
            print(getVarValue(splitLine[i + 1]))
        i = i + 1
    
    ############ actual operations on the line ########################
    if runOperations: # really only a way to reduce running unnecessary lines
        i = 0
        while i < len(splitLine): #for i in range(len(splitLine)):
            if splitLine[i] == "->":
                left = splitLine[i - 1]
                if currentVarType == 3:                           # string
                    if splitLine[i - 1].isnumeric():              # convert constant to char
                        left = chr(int(splitLine[i - 1]))
                elif currentVarType == 1:                         # int 
                    left = int(splitLine[i - 1])
                setVarValue(splitLine[i + 1], left)
            if splitLine[i] == "+" or splitLine[i] == "-" or splitLine[i] == "cr" or splitLine[i] == "/":
                if splitLine[i] == "+":                           # +
                    splitLine[i + 1] = addition(splitLine[i - 1], splitLine[i + 1], currentVarType)                 
                elif splitLine[i] == "-":                         # -
                    splitLine[i + 1] = subtraction(splitLine[i - 1], splitLine[i + 1], currentVarType)
                elif splitLine[i] == "cr":
                    splitLine[i + 1] = multiplication(splitLine[i - 1], splitLine[i + 1], currentVarType)
                elif splitLine[i] == "/":
                    splitLine[i + 1] = division(splitLine[i - 1], splitLine[i + 1], currentVarType)
                splitLine.pop(i - 1)
                splitLine.pop(i - 1)
                i = i - 1
            i = i + 1
                
f.close()        
            
            
            
            
            
            
            
            