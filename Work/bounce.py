# bounce.py
#
# Exercise 1.5
height = 100.00
bounces = 0

while bounces < 10:
    bounces = bounces +1
    height = height * 3/5
    print (bounces,round(height,2))
