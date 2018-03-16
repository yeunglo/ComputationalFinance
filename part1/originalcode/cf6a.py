# import csv
import pandas as pd
# import quandl
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./stocks30.csv', index_col = 'Date')

# calculate daily and annual returns of the stocks
returns_daily = data.pct_change()
returns_one = returns_daily.mean()
# print('returns:',returns_one)

# get daily and covariance of returns of the stock
covariance = returns_daily.cov()
# print('covariance:',covariance)

# empty lists to store returns, volatility and weights of imiginary portfolios
port_returns = []
port_volatility = []
sharpe_ratio = []
stock_weights = []

# set the number of combinations for imaginary portfolios
num_portfolios = 5000
num_assets = 6

for single_portfolio in range(num_portfolios):

    weights = np.random.random(num_assets)
    weights /= np.sum(weights)

    # print(weights)

    weights = list(weights)
    # print(weights)

    zeros = np.zeros(24,int)
    zeros = list(zeros)

    weights.extend(zeros)
    np.random.shuffle(weights)
    # print(weights)

    weights = np.array(weights)
    # print(weights)

    returns = np.dot(weights, returns_one)

    volatility = np.sqrt(np.dot(weights.T, np.dot(covariance, weights)))
    sharpe = returns / volatility
    sharpe_ratio.append(sharpe)
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)


print(stock_weights[1])

# a dictionary for Returns and Risk values of each portfolio
portfolio = {'Returns': port_returns,
             'Volatility': port_volatility,
             'Sharpe Ratio': sharpe_ratio}

# extend original dictionary to accomodate each ticker and weight in the portfolio
for counter,symbol in enumerate(['SDR.L', 'NMC.L', 'CPG.L', 'BT', 'SHP.L', 'PRU.L', 'SKY.L', 'BNZL.L', 'STJ.L', 'TSCO.L', 'EZJ.L', 'GFS.L', 'CCL.L', 'EXPN.L', 'RSA.L', 'SMIN.L', 'SSE.L', 'CNA.L', 'TUI.L', 'CCH.L', 'RTO.L', 'VOD.L', 'BATS.L', 'AHT.L', 'PPB.L', 'BRBY.L', 'ANTO.L', 'DLG.L', 'UU.L', 'BCS']):
    portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

# make a nice dataframe of the extended dictionary
portfolios = pd.DataFrame(portfolio)

print(portfolios)

# get better labels for desired arrangement of columns
column_order = ['Returns', 'Volatility', 'Sharpe Ratio'] + [stock+' Weight' for stock in ['SDR.L', 'NMC.L', 'CPG.L', 'BT', 'SHP.L', 'PRU.L', 'SKY.L', 'BNZL.L', 'STJ.L', 'TSCO.L', 'EZJ.L', 'GFS.L', 'CCL.L', 'EXPN.L', 'RSA.L', 'SMIN.L', 'SSE.L', 'CNA.L', 'TUI.L', 'CCH.L', 'RTO.L', 'VOD.L', 'BATS.L', 'AHT.L', 'PPB.L', 'BRBY.L', 'ANTO.L', 'DLG.L', 'UU.L', 'BCS']]

# reorder dataframe columns
portfolios = portfolios[column_order]

# find min Volatility & max sharpe & max MV values in the dataframe (df)
min_volatility = portfolios['Volatility'].min()
max_sharpe = portfolios['Sharpe Ratio'].max()

# use the min, max values to locate and create the three special portfolios
sharpe_portfolio = portfolios.loc[portfolios['Sharpe Ratio'] == max_sharpe]
min_variance_port = portfolios.loc[portfolios['Volatility'] == min_volatility]

# print the details of the 2 special portfolios
print(min_variance_port.T)
print(sharpe_portfolio.T)
# print(pd.merge((pd.merge(min_variance_port.T, sharpe_portfolio.T,left_index=True, right_index=True, how='inner')), mv_portfolio.T, left_index=True, right_index=True, how='inner'))
# find max(expected return - risk)