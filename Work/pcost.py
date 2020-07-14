# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):

    with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(row)
        headers = next(row)
        total = 0.0
        for rows in row:
            try:
                nshares = int(fields[1])
                price = float(row[2])
                total += nshares * price

            except ValueError:
                print("Bad row", line)

    print('Total', total)

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost('Data/portfolio.csv')
print('Total', cost)   