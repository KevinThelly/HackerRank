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
        # print(i)
        if(c[i+1]==1):
            i=i+2
            jump=jump+1
        elif(c[i+1]==0):
            # print("i+1=0")
            if(i+2<len(c)):
                if(c[i+2]==0):
                    # print("i+2=0")
                    i=i+2
                    jump=jump+1
                    continue
            if(c[i+1]==0):
                # print("i+1=0")
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
