#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:05:23 2020

@author: andreamarin
"""

import json

myfile = open('657354.json')

data = json.load(myfile)


# =============================================================================
# # transactions = data['blocks'][0]['tx']
# =============================================================================
transactions = data['blocks'][0]['tx']


listofblocks  = data['blocks']

block = listofblocks[0]

listoftransactions = block['tx']


print(len(listoftransactions))






# =============================================================================
# #create a list of strings that contains all the
# #hashcodes associated with the block's transactions
# 
# #I must begin with the empty list
# =============================================================================
l = []

for el in listoftransactions:
    #I want to add to l the field 'hash'
    l.append(el['hash'])

# print(l) print the list of all the transaction hash codice




#excluding the origin at index 0 for possiblity of accessing the input values 
#from 'prev_out' key,

del listoftransactions[0]






# =============================================================================
# 
# create a list of strings that contains all the
# inputs associated with the block's transactions
# 
# I must begin with the empty list
# =============================================================================
inV = [] 

for el in listoftransactions:
    #I want to add to l the field 'hash'
    inV.append(el['inputs'][0]['prev_out']['value'])
   

#print(inV)

#length of transactions
print()
print(f'The total number of inputs are is {len(inV)} excluding the \nposition index zero, which is the origin.')
print(50*'_')





# =============================================================================
# 
# #performing simple stat
# =============================================================================
import statistics


avg = round(statistics.mean(inV),2) #average value of total the total transactions moved



maxI = max(inV) #the maximum value of input done
minI = min(inV) #the minimum value of input done

#position of the maximum input
maxPosition = inV.index(maxI) 

# Indexing the positions the maximum and minimum input values from the list for hash variable l
# maxl =l.index('a60d87388f658ee8f6f371ed6fff6f810bd12c31304f6b4f020f80a4e70b7061')
# print(maxl)
# minl = l.index('f5d0a2be813539737145307fbbc47b14d551f5b046df2078e00708c62ec7de55')
# print(minl)

print(f'The position of the maximum value transacted is {maxPosition}.')
print()


#position of the minimum input
minPosition = inV.index(minI) 
print(f'The position of the minimum value transacted is {minPosition}.') 
print()



#visualizing the data with matplotlib plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array(inV)

plt.plot(x)
plt.grid(color='k', linestyle='-', linewidth= 0.1)
plt.show() 

print()
print(10*'*','Simple statistical analysis',10*'*')
print(f'The average amount of input is {avg}.')
print(f'The max amount of input is {maxI}.')
print(f'The min amount of input is {minI}.')








# =============================================================================
# #create a list of strings that contains all the
# #outputs associated with the block's transactions
# 
# #I must begin with the empty list
# =============================================================================
# =============================================================================
# outputValues = []
# 
# for el in listoftransactions:
#     #I want to add to l the field 'inputs'
#     outputValues.append(el['out'][0:]['value'])
# 
# print(outputValues)
# =============================================================================






