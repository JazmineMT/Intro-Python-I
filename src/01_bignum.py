# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
import math 

try:
    answer=math.pow(2.0,65536)

except OverflowError :
    answer = 'Input value is greater than the allowed limit'


print(answer)

# print( math.pow(2.0,65536))

