# Read two integer numbers, X and Y
x, y = map(int, input().split())

# Determine the larger and smaller of the two numbers
if x > y:
    greater = x
    smaller = y
else:
    greater = y
    smaller = x

# Print all numbers from the greater to the smaller, in descending order
for i in range(greater, smaller - 1, -1):
    print(i)