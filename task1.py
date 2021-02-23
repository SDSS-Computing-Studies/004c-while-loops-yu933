#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
import math
import time

targetNum = 20
count = 2

print("The target is " + str(targetNum))
print("===================")
while targetNum == 20:
    print(count)
    count = count + 2
    # time.sleep(x) will pause the program at this point for x seconds where x is a float 
    time.sleep(0.01)
    if count > 20:
        break
print("===================")