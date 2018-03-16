#!python3


import csv
import pandas as pd
# import quandl
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot
# pyplot.use('TkAgg')
# import os

data = pd.read_csv('./stocks30.csv', index_col = 'Date')
# print(data)
trainset = data.iloc[0:378]
testset = data.iloc[378:756]


trainset_three = trainset.loc[:,['CCH.L', 'PPB.L', 'CPG.L']]
testset_three = testset.loc[:,['CCH.L', 'PPB.L', 'CPG.L']]
# print(trainset_three)
# print(testset_three)
'''
# mean = np.mean()
# means = []
means = pd.DataFrame(columns=['mean'])
for i in trainset.columns:
    mean = np.mean(trainset.loc[:,[i]])
    # print(mean)
    # means.append(mean)
    mean = pd.DataFrame(data=mean, columns=['mean'])
    means = means.append(mean, ignore_index=True)
    # print(mean)
# for j in range(len(mean)):
#     means = pd.concat([mean], axis=0)

print(means)
'''


# trainset.index.name = 'date'
# traintable = trainset.pivot(columns='ticker')
# print('table:',trainset_three)

# calculate daily and annual returns of the stocks
returns_daily = trainset_three.pct_change()
returns_one = returns_daily.mean()
# print(trainset.pct_change())
# print('returns:',returns_one)
# returns_annual = returns_daily.mean() * 250

# get daily and covariance of returns of the stock
covariance = returns_daily.cov()
# cov_annual = cov_daily * 250
# print('covariance:',covariance)

# empty lists to store returns, volatility and weights of imiginary portfolios
port_returns = []
port_volatility = []
sharpe_ratio = []
mv_model = []
stock_weights = []

# set the number of combinations for imaginary portfolios
num_assets = 3
num_portfolios = 5000

# populate the empty lists with each portfolios returns,risk and weights
for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    # print('w1:', weights)
    weights /= np.sum(weights)
    # print('w2:', weights)
    returns_three = np.dot(weights, returns_one)
    volatility = np.sqrt(np.dot(weights.T, np.dot(covariance, weights)))
    sharpe = returns_three / volatility
    mv = returns_three - np.dot(0.5,volatility)
    mv = returns_three - np.dot(0.5, volatility)
    mv_model.append(mv)
    sharpe_ratio.append(sharpe)
    port_returns.append(returns_three)
    port_volatility.append(volatility)
    stock_weights.append(weights)

# a dictionary for Returns and Risk values of each portfolio
portfolio = {'Returns': port_returns,
             'Volatility': port_volatility,
             'Sharpe Ratio': sharpe_ratio,
             'MV Model': mv_model}

# extend original dictionary to accomodate each ticker and weight in the portfolio
for counter,symbol in enumerate(['CCH.L', 'PPB.L', 'CPG.L']):
    portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

# make a nice dataframe of the extended dictionary
portfolios = pd.DataFrame(portfolio)

print(portfolios)

# get better labels for desired arrangement of columns
column_order = ['Returns', 'Volatility', 'Sharpe Ratio', 'MV Model'] + [stock+' Weight' for stock in ['CCH.L', 'PPB.L', 'CPG.L']]

# reorder dataframe columns
portfolios = portfolios[column_order]
# print(portfolios)

# find min Volatility & max sharpe & max MV values in the dataframe (df)
min_volatility = portfolios['Volatility'].min()
max_sharpe = portfolios['Sharpe Ratio'].max()
max_mv = portfolios['MV Model'].max()
print()
# use the min, max values to locate and create the three special portfolios
sharpe_portfolio = portfolios.loc[portfolios['Sharpe Ratio'] == max_sharpe]
min_variance_port = portfolios.loc[portfolios['Volatility'] == min_volatility]
mv_portfolio = portfolios.loc[portfolios['MV Model'] == max_mv]

# print the details of the 2 special portfolios
print(min_variance_port.T)
print(sharpe_portfolio)
print(mv_portfolio.T)
# print(pd.merge(min_variance_port.T, sharpe_portfolio.T,left_index=True, right_index=True, how='inner'))
print(pd.merge((pd.merge(min_variance_port.T, sharpe_portfolio.T,left_index=True, right_index=True, how='inner')), mv_portfolio.T, left_index=True, right_index=True, how='inner'))
# find max(expected return - risk)


# plot the efficient frontier with a scatter plot
plt.style.use('seaborn-dark')
# portfolios.plot.scatter(x='Volatility', y='Returns', figsize=(10, 8), grid=True)
portfolios.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
                cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
s = plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'],
            c='orange', marker='X', s=200, )
v = plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'],
            c='red', marker='X', s=200 )
m = plt.scatter(x=mv_portfolio['Volatility'], y=mv_portfolio['Returns'],
            c='fuchsia', marker='X', s=200 )

plt.legend((s, v, m),('Max Sharpe Ratio', 'Min Risk','Max MV Model'), scatterpoints=1, loc='upper left', ncol=3, fontsize=8)

plt.axis([0.01, 0.022, 0.00075, 0.0025])
plt.xlabel('Risk (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')
plt.show()

# plot frontier, max sharpe & min Volatility values with a scatterplot
# plt.style.use('seaborn-dark')
# portfolios.plot.scatter(x='Volatility', y='Returns', c='Sharpe Ratio',
#                 cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
# plt.scatter(x=sharpe_portfolio['Volatility'], y=sharpe_portfolio['Returns'], c='red', marker='D', s=200)
# plt.scatter(x=min_variance_port['Volatility'], y=min_variance_port['Returns'], c='blue', marker='D', s=200 )
# plt.xlabel('Volatility (Std. Deviation)')
# plt.ylabel('Expected Returns')
# plt.title('Efficient Frontier')
# plt.show()


# p-value
# from scipy.stats import chisquare
# f_obs = [23, 17, 50]
# f_exp = [30, 30, 30]
# chisq, p = chisquare(f_obs, f_exp)
# print chisq
# print p
