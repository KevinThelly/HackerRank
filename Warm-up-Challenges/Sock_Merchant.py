#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result=0
    for i in range(n):
        temp=ar[i]
        ar[i]=-1
        if temp in ar:
            index1=ar.index(temp)
            if(ar[index1]!=-1):
                result=result+1
            ar[index1]=-1
            
    return result
            

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
