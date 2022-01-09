# -*- coding: utf-8 -*-
"""
Super simple implementation of rallyLang
"""

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

variables = []

fileName = ""
f = open("Test Files/HelloWorld.txt", "r")

Lines = f.read()
Lines = Lines.replace("\t", "\n") # new line is acceptable separator and so is tab, so combine them
Lines = Lines.split("\n") # split the input into the commands

for line in Lines:
    splitLine = line.split(" ")
    ###### line preprocess ############
    currentVarType = 0 # 0 = int, 2 = double, 3 = string
    leftOfInto = True
    runOperations = True
    for i in range(len(splitLine)):
        try:
            if "slpy" in splitLine[i]:   
                variables.append(Variable(3, "", splitLine[i + 1]))
                splitLine.pop(i)
                currentVarType = 3
                i = 0
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
        except:
            j = 0
    
    ############ actual operations on the line ########################
    if runOperations: # really only a way to reduce running unnecessary lines
        i = 0
        while i < len(splitLine): #for i in range(len(splitLine)):
            if splitLine[i] == "->":
                left = splitLine[i - 1]
                if currentVarType == 3: 
                    if splitLine[i - 1].isnumeric():
                        left = chr(int(splitLine[i - 1]))
                    setVarValue(splitLine[i + 1], left)
            elif splitLine[i] == "+":
                left = splitLine[i - 1]
                right = splitLine[i + 1]
                if currentVarType == 3: 
                    if splitLine[i - 1].isnumeric():
                        left = chr(int(splitLine[i - 1]))
                    if splitLine[i + 1].isnumeric():
                        right = chr(int(splitLine[i + 1]))
                splitLine[i + 1] = left + right
                splitLine.pop(i - 1)
                splitLine.pop(i - 1)
                i = i - 1
            i = i + 1
                
f.close()        
            
            
            
            
            
            
            
            