# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fe701ErLyXZzyIxuVbaP90CPiUu0nPqo
"""

#Madlib game
print('Please answer the questions below')
e2014 = input('Name of 2014 epidemic in West Africa: ')
p2020 = input('Name of the 2020 pandemic disease: ')
oC19 = input('Where was Covid-19 first reported: ')
highD = input('Name of the country with highest Covid-19 deaths: ')
euroEc = input('The first epicenter of covid-19 in  Europe: ')
southA = input('Name of the South American country with highest deaths: ')
robS = input('Name of police squared that totured people in Nigeria:')

              #Answers in a sentence
def Madlib():
  print('1.' + e2014 + ' is the name of the epidemic in West Africa.')
  print('2.' + p2020 + ' is the name of the current pandemic.')
  print('3.' + oC19 + ' was where the first clusters of covid-19 was detected.')
  print('4.' + highD + ' have the higest toll deaths of the coronavirus.')
  print('5.' + euroEc + ' is the first epicenter of covid-19 in Europe.')
  print('6.' + southA + ' is the name of the country with highest number \n of death in South America.')
  print('7.' + robS + ' is the name of the police Squad. #End_SARs_Now ')


print('\n \n \n')


print('Bravo below is your MADLIB GAME!')
print('\n')
Madlib()

#Mutiplication table code

print('Multiplication Table')
for i in range(1 ,13):
  for j in range(1, 13):
    print('{0} times {1} is: {2}'.format(i,j,i*j))
  print('-----------------------')

#creating a quadractic function----------------------------------------------
import math
def quad(a,b,c):
    delta = b*b - 4*a*c
    if delta >= 0:
        v = math.ceil((-b + math.sqrt(delta))/(2*a))
        w = math.ceil((-b - math.sqrt(delta))/(2*a))
        res= v , w
    else:
        res='Complex negative number'
    
    return res
    print('The quadractic variables are: {0} & {1} repectively'.format(v,w))
    

quad(-2,1,5) #input vales for a,b c and calling the function.