from math import ceil, floor, exp, fabs, log, log10, modf, sqrt, pi, cos, tan, degrees, radians

#absolute value
print(abs(-85))
print(fabs(-85))
#ceiling and floor
print(ceil(48.9))
print(floor(48.9))
#exponential
print(exp(4))
#log
print(log(10))
print(log10(10))
#maximum and minimum
print(max(3,425,34,100))
print(min(3,425,34,100))
#fractonal and integer part of number
print(modf(56.998340))
#Power,Square root,Round
print(pow(3,2))
print(sqrt(36))
print(round(45.6))

#Random Number Functions
from random import choice, randrange, random, shuffle, uniform

values=[23,55,5,78,12]
#Choice
print(choice(values))

#A randomly selected element from range(start, stop, step)
print(randrange(5,25,4))

#A Random float value
print(random())

#Randomizes the items of a list in place.
shuffle(values)
print(values)

#A random float r, such that x is less than or equal to r and r is less than y
print(uniform(2,5))

#Trigonometric Functions

print(cos(0))
print(tan(pi/4))

#Converts angle x from radians to degrees.

print(degrees(pi/4))

#Converts angle x from degrees to radians.
print(radians(90))
