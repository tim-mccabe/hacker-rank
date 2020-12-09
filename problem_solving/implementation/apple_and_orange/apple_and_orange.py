#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    c = 0
    d = 0
    n_apples = [x + a for x in apples]
    n_oranges = [y + b for y in oranges]
    # loop through apples
    for i in n_apples:
        if s <= i <= t:
            c += 1
    for j in n_oranges:
        if s <= j <= t:
            d += 1
    print(c)
    print(d)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)