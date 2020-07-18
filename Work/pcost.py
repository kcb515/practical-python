# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):

    total = 0.0
    with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=2):
            record = dict(zip(headers,row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares * price

            except ValueError:
                print(f'Row{rowno}: Bad row: {row}')

    print('Total', total)

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfolio.csv')
print('Total', cost)   