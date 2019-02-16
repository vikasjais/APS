#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip()) - 1
    
    n1 = n // 3
    n2 = n // 5
    n3 = n // 15
    
    sumOf3 = (n1 * (n1+1) >> 1) * 3
    sumOf5 = (n2 * (n2+1) >> 1 ) * 5
    sumOf15 = (n3 * (n3+1) >> 1) * 15
    
    print(int(sumOf3 + sumOf5 - sumOf15))
