Given an integer,n , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input().strip())
if (N % 2 == 0) and (N >= 2) and (N <= 5):
    print('Not weird')
elif (N % 2 == 0) and (N >= 6) and (N <= 20):
    print('Weird')
elif N>20 :
    print ('Not Weird')
else: 
    print ('Weird')
