#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    val=0
    for i in q[:len(q)-1]:
        dif=i-q.index(i)-1
        if(dif>2):
            return "Too chaotic"
        else:
            # print(i)
            if(i>q[q.index(i)+1] or q.index(i)<i):
                if(dif>0):
                    val=val+dif
                else:
                    val=val-dif
        print("test",i,dif,val)
            
    return val


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        val=minimumBribes(q)
        print(val)
