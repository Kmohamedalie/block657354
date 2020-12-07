#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 12:05:23 2020

@author: andreamarin
"""

                              #NOTE
# =============================================================================
# ***please download the json file of the bloock 657354 from
# this link https://github.com/Kmohamedalie/block657354/blob/main/657354.json
# 
# ****** IN other to run your code you must save both  the json  file and the
#  python file in the same directory/folder and run the script and explore
#  
# =============================================================================
 


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








#Solution 1. Easy level
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

bitC = 100000000

print()
print(10*'*','Simple statistical analysis',10*'*')
print(f'1.The average amount of input is {avg} and {avg/bitC} in BTC.')
print(f'2.The max amount of input is {maxI} and {maxI/bitC} in BTC.')
print(f'3.The min amount of input is {minI} and {minI/bitC} in BTC.')


#visualizing the data with matplotlib plot
import matplotlib.pyplot as plt
import numpy as np

x = np.array(inV)
y = np.array(maxI)
maxPosition = inV.index(maxI)
minPosition = inV.index(minI)  


plt.plot(x)
plt.plot(maxPosition,maxI,'r*') #indicating a red star for the minimum value transacted in the block which is 546.
plt.plot(minPosition,minI,'r*') #indicating a red star for the minimum value value transacted in the block which is 43119903723.
plt.ylabel('Input values') #label for the y-axis
plt.xlabel('index') #label for the x-axis
plt.suptitle('A Plot of all input values') #Main title of the plot
plt.grid(color='k', linestyle='-', linewidth= 0.1) #grids on for simple visualization
plt.show() #display the plot








#Solution 2.  Intermediate to advance
# =============================================================================
# Creating a dataframe using the hash and input values 
# =============================================================================

''' Please run this section line by line'''

# importing pandas as pd 
import pandas as pd 
 

hashCode = list(l) #creating a new list  containing hashcodes
del hashCode[0]     #deleting hash code at the origin or index 0 
input_Values = list(inV) #creating a new list  containing input values

# dictionary of lists 
dict = {'hashCode': hashCode, 'inputs_Values': input_Values} 
	
df = pd.DataFrame(dict) 

# saving the dataframe 
df.to_csv('657354.csv') 

#opening and reading the dataframe
btc = open('657354.csv')
btc1 = pd.read_csv(btc)

#exploring the data first/last values with head,tail and describe function for quick summary.
btc1.columns = ['index','hash','inputValues'] #renaming the columns
btc1.head(); head = btc1.head() 
btc1.tail(); tail = btc1.tail()
btc1.describe(); summary_statistics = btc1.describe()
print(f'''
   ****************  head  ********************
   {head}
   
   
   
   ***************  Tail   *******************
   {tail}
   
   
   
   *******  summary_statistics **************
   {summary_statistics}
  ''')

