#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    jump=0
    while(i<len(c)-1):
        if(c[i+1]==1):
            i=i+2
            jump=jump+1
        elif(c[i+1]==0):
            if(c[i+2]==0):
                i=i+2
            else:
                i=i+1
            jump=jump+1
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
