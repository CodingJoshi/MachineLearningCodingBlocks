# SysModule.py

import sys
def printData():
	print(sys.argv)

def printSum():
	print(int(sys.argv[1])+int(sys.argv[2]));

printSum()

print(sys.version)

print(sys.path)

# print(sys.maxint)
print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)

To visualize the recursive codes:
I would suggest two points:

Create a stack and keep pushing the function calls inside the stack one above another and for each return statement, pop it out of the stack.

Do not take a large example as it would take too long and might confuse you.
Thus, rather take a small example where the total recursive calls will be less.

This, way you would be able to understand the concept.