# import math

product = 1
sum = 0

# n factorial loop.
for i in range(1, 101):				# can also use math.fatorial(100) instead of this loop.
    product *= i
    
# lets sum all of the digit in the product,
# by converting the number into a string we can iterate over each character in the string.
for d in str(product):
    sum += int(d)
    
print(sum)