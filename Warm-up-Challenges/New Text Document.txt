#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    result=0
    valleys=0
    for i in s:
        temp=result
        if(i=='U'):
            result=result+1
        else:
            result=result-1

        # print(i,result)
        if(result==0):
            if(temp==-1):
                valleys=valleys+1
    if(result==-1):
        valleys=valleys+1
    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
