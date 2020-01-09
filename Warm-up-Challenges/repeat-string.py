#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    sum=0
    length=0
    for i in s:
        if(i=='a'):
            sum=sum+1

    size=len(s)
    repeat=n//size
    remainder=n%size

    for i in s[:remainder]:
        if(i=='a'):
            length=length+1

    sum=sum*repeat
    sum=sum+length
    return int(sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
