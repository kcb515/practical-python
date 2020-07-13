# pcost.py
#
# Exercise 1.27
total = 0.0

with open('portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares= int(row[1])
        price = float(row[2])
        total += nshares * price

print('Total', total)
    