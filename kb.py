#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Knowledge base Assisgnment"""
"""
Created on Sun Apr 11 00:19:07 2021

@author: indeshwar chaudhary
"""

import sys
import re


def dictionary(listD): 
    dictA = {}                         #create an empty dictionary
    for i in range(1, len(listD)):
        r = listD[i].split("=")        #seperated the key value pairs from '='
        
        if re.findall('T', listD[i]):  #if key has value T, assign True as value in dictA
            dictA[r[0]] = True
    
        elif re.findall('F', listD[i]): #if key has value F, assign False as value in dictA
            dictA[r[0]] = False
  
    return dictA


#convert the infix notation into postfix
def postfix(listA, k):
    stack = []                        #create an empty stack
    listB = []                        #create an empty list that store postfix value notation
    listC = ['(', 'V', '^']  
    for i in listA:
        if i in listC:      
            stack.append(i)           # push '(', 'V', '^' in stack
        
        elif i != ')' and re.findall('~', i):  #push negation variable in listB
            listB.append(i)
        
        elif i != ')' and i in k:
            listB.append(i)             #append all the variables in the listB
            
        elif i == ')':               
            while(True):
                if len(stack)!= 0:      #if the stack not empty,
                    p = stack.pop()     #pop the special ('(', 'V', '^') symbols from stack
                    if p != '(':
                        listB.append(p) #append special symbol in the listB
        
                else:
                    break
            
              
    return listB
            

def knowledge_base(listC, dictA, k):
    l = ['V', '^']
    stack = []     #create an empty stack
    for x in listC:
        if x not in l and x in k:
            stack.append(dictA[x]) #push the values of x in stack which are boolean value
            
        elif x not in l and re.findall('~', x):
            n = x.split('~') 
            stack.append((not dictA[n[1]])) #push the negation value in the stack
            
        else:                      #if 'V' or '^' found in listC, pop p1 and p2
            p1 = stack.pop()         
            p2 = stack.pop()
            
            if x == 'V':           # if x is 'V',
                result = p1 or p2       #compute OR logic
                stack.append(result)    #push the result back in stack
            
            elif x == '^':         # if x is '^',
                result = p1 and p2      #compute AND logic
                stack.append(result)    #push the result back in stack
                
       
    p = stack.pop()
    print(p)

#read the complex sentence and convert into list
def abc(listD):
    listA = listD.split(" ") 
    listE = []
    for w in listA:
        if '(' in w:
            listE.append('(')
            w1 = w.split('(')
            listE.append(w1[1])
       
        elif ')' in w:
            w2 = w.split(')');
            listE.append(w2[0])
            listE.append(')')
            
        else:
            listE.append(w)
       
           
            
    return listE


file_name = sys.argv[1]
file = open(file_name, 'r')




def main(file):
   
    while file:
        lines = file.readline()
        if lines == "":                     #if lines is null, break
            break
        listD = lines.split(",")            #split the lines 
                
        listA = abc(listD[0])               #read the complex sentence and convert into list                   
        
        dictA = dictionary(listD)           #create a dictionary that assigns variables as key and values as True or False
        k = dictA.keys()                    #k is list of all keys
        listC = postfix(listA, k)           #convert infix notation into postfix notation
        knowledge_base(listC, dictA, k)     #evaluate the sentence
        
       
        
        
main(file)
    








        

