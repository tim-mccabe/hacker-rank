#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if int(n) % 2 == 1:
        print('Weird')
    if 2 <= int(n) <= 5 and int(n) % 2 == 0:
        print('Not Weird')
    if 6 <= int(n) <= 20 and int(n) % 2 == 0:
        print('Weird')
    if int(n) > 20 and int(n) % 2 == 0:
        print('Not Weird')
