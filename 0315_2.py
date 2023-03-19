import csv

def read_portfolio(filename):
    portfolio =[]

    with open('portfolio.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            stock = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(stock)

    return portfolio

def read_prices(filename):

    prices = {}
    with open(filename) as f:
        row = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return prices

portfolio = read_portfolio('portfolio.csv')
prices = read_prices('prices.csv')

total_cost = 0.0

total_value = 0.0

print('Current value', total_value)

print('Gain', total_value - total_cost)