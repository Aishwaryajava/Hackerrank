# Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of  to , print Not Weird
If n is even and in the inclusive range of  to , print Weird
If n is even and greater than , print Not Weird

#!/bin/python3
#solution 1
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
if n % 2!= 0 or (n>=6 and n<=20):
    print("Weird")
else:
    print("Not Weird")
    
#solution 2
#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")




