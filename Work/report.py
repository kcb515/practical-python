# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    '''Read in the holdings from portfolio'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0],
                       'shares': int(row[1]),
                       'price' : float(row[2])
                       }
            portfolio.append(holding)
            
    return portfolio

def read_prices(filename):
    prices = {}

    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]] = row[1]
        except IndexError:
            pass
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')


def make_report(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price,change)
        rows.append(summary)
    return rows

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')