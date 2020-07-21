# report.py
#
# Exercise 2.4
import csv
import fileparse
from fileparse import parse_csv

portfolio = fileparse.parse_csv(filename,select=['name','shares','price'], types=[str,int,float])  
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


def make_report_data(portfolio, prices):
    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock[['price']]
        summary = (stock['name'], stock['shares'], current_price,change)
        rows.append(summary)
    return rows

def print_report(report):

    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-'* 10 + ' ') * len(headers))
    for report in report:
        print('%10s %10d %10.2f %10.2f' % row)
def portfolio_report(portfolio_filename, prices, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = make_report_data(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv','Data/prices.csv')

print('My _name_ is', __name__)