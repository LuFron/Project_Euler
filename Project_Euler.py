# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 08:25:39 2021

@author: fronortin_l
"""
import math

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def Euler_18(triangle):
    #Transformation de la chaîne de caractère en une liste contenant
    #des sous listes (représentant les lignes) qui contiennent
    #les nombres de chaque ligne
    triangle = [[int(j) for j in i.split()] for i in triangle.split("\n")]
    #Inversion de la liste triangle
    triangle.reverse()
    #Teste de toutes les valeurs à partir de la seconde ligne
    #pour trouver quel est la somme maximale possible en partant de ces valeurs
    for i in range(1, len(triangle)):
        for j, k in enumerate(triangle[i]):
            triangle[i][j] = k + max([triangle[i-1][j], triangle[i-1][j+1]])
    return triangle[-1][0]

  
def Euler_19():
  dico = {'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
  year = 1901
  day = 2
  sunday = 0
  
  while year !=2001:
    for i in dico:
      day += dico[i]
      
      if (i == 'February') and (year%4==0 or (year%100==0 and year%400==0)):
        day +=1
        
      day = day%7
      
      if day==0:
        sunday+=1
        day =7
        
    year+=1
  
  return sunday 

def sum_factors(n):  
     result = []
     for i in range(1, int(n**0.5) + 1):
         if n % i == 0:
             result.extend([i, n//i])
     return sum(set(result)-set([n]))

def Euler_21(number):
    result = []
    for x in range(1,number+1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result.append(tuple(sorted((x,y))))
    
    return sum([sum(i) for i in set(result)])

def Euler_22():
    with open('D:\p022_names.txt') as f:
        lines = f.readlines()

    lines= lines[0].split(',')
    lines = [i.replace('"','') for i in lines]
    lines.sort()

    for k,i in enumerate(lines):
        s=0
        for j in i:
            s+= ord(j)-64
            lines[k] = s
    
    return sum([lines[i]*(i+1) for i in range(len(lines))])















