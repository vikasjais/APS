#!/usr/bin/env python
# coding: utf-8

def isPower2(n):
    return True if n & n -1 == 0 else False

def calcSetBits(n):
    result = 0
    while n:
        result += 1
        n &= n -1
    return result

def isEven(n):
    return True if n & 1 == 0 else False 

def divisibleByEight(n):
    return True if (n >> 3)<<3 == n else False

def LIS(arr):
    
    aux = [1]*len(arr)
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[i] > arr[j] and aux[j] + 1 > aux[i]:
                aux[i] += 1
    return max(aux)

