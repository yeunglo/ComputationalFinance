

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
# trainset = data.iloc[0:378]
testset = data.iloc[378:756]
testset_three = testset.loc[:,['CCH.L', 'PPB.L', 'CPG.L']]

weights = pd.read_csv('./picked_three.csv', index_col = 'Portfolio NO.')
weights = weights.T
# print(weights)
# print(weights.ix[5:8,[43]])
weights_sharpe = weights.ix[5:8,[43]]
weights_risk = weights.ix[5:8,[873]]
weights_mv = weights.ix[5:8,[3791]]
weights_naive = np.array([1/3,1/3,1/3],dtype=np.float)


# calculate daily and annual returns of the stocks
returns_daily = testset_three.pct_change()
returns_one = returns_daily.mean()
# print(trainset.pct_change())
print('returns:',returns_one)
# returns_annual = returns_daily.mean() * 250

# get daily and covariance of returns of the stock
covariance = returns_daily.cov()
# cov_annual = cov_daily * 250
print('covariance:',covariance)

# returns_sharpe = np.dot(weights[], returns_one)

# empty lists to store returns, volatility and weights of imiginary portfolios
port_returns_s = []
port_returns_r = []
port_returns_m = []
port_volatility_s = []
port_volatility_r = []
port_volatility_m = []
sharpe_ratio_s = []
sharpe_ratio_r = []
sharpe_ratio_m = []
mv_model = []
stock_weights = []

# set the number of combinations for imaginary portfolios
num_assets = 3
num_portfolios = 5000
'''
# populate the empty lists with each portfolios returns,risk and weights
for single_portfolio in range(num_portfolios):
    # weights = np.random.random(num_assets)
    # print('w1:', weights)
    # weights /= np.sum(weights)
    # print('w2:', weights)
    returns_sharpe = np.dot(weights_sharpe.T, returns_one)
    returns_risk = np.dot(weights_risk.T, returns_one)
    returns_mv = np.dot(weights_mv.T, returns_one)
    # print(weights_sharpe.T)
    # print(np.dot(weights_sharpe.T, np.dot(covariance, weights_sharpe)))
    # volatility_sharpe = np.sqrt(np.dot(weights_sharpe.T, np.dot(covariance, weights_sharpe)))
    # volatility_risk = np.sqrt(np.dot(weights_risk, np.dot(covariance, weights_risk.T)))
    # volatility_mv = np.sqrt(np.dot(weights_mv, np.dot(covariance, weights_mv.T)))
    volatility_sharpe = np.dot(weights_sharpe.T, np.dot(covariance, weights_sharpe))
    volatility_risk = np.dot(weights_risk.T, np.dot(covariance, weights_risk))
    volatility_mv = np.dot(weights_mv.T, np.dot(covariance, weights_mv))
    sharpe_s = returns_sharpe / volatility_sharpe
    print(sharpe_s)
    sharpe_r = returns_risk / volatility_risk
    sharpe_m = returns_mv / volatility_mv
    # mv = returns_three - np.dot(0.5,volatility)
    # mv = returns_three - np.dot(0.5, volatility)
    # mv_model.append(mv)
    sharpe_ratio_s.append(sharpe_s)
    sharpe_ratio_r.append(sharpe_r)
    sharpe_ratio_m.append(sharpe_m)
    # port_returns_s.append(returns_sharpe)
    # port_returns_r.append(returns_risk)
    # port_returns_m.append(returns_mv)
    # port_volatility.append(volatility)
    # stock_weights.append(weights)
'''

returns_sharpe = np.dot(weights_sharpe.T, returns_one)
returns_sharpe = returns_sharpe[0]
# print(returns_sharpe)
returns_risk = np.dot(weights_risk.T, returns_one)
returns_risk = returns_risk[0]
returns_mv = np.dot(weights_mv.T, returns_one)
returns_mv = returns_mv[0]

volatility_sharpe = np.dot(weights_sharpe.T, np.dot(covariance, weights_sharpe))
volatility_sharpe = volatility_sharpe[0]
volatility_sharpe = volatility_sharpe[0]
volatility_sharpe = np.sqrt(volatility_sharpe)
# print(volatility_sharpe)
volatility_risk = np.dot(weights_risk.T, np.dot(covariance, weights_risk))
volatility_risk = volatility_risk[0]
volatility_risk = volatility_risk[0]
volatility_risk = np.sqrt(volatility_risk)
volatility_mv = np.dot(weights_mv.T, np.dot(covariance, weights_mv))
volatility_mv = volatility_mv[0]
volatility_mv = volatility_mv[0]
volatility_mv = np.sqrt(volatility_mv)

returns_naive = np.dot(weights_naive.T, returns_one)
volatility_naive = np.sqrt(np.dot(weights_naive, np.dot(covariance, weights_naive.T)))

sharpe_s = returns_sharpe / volatility_sharpe
print(sharpe_s)
sharpe_r = returns_risk / volatility_risk
print(sharpe_r)
sharpe_m = returns_mv / volatility_mv
print(sharpe_m)
sharpe_naive = returns_naive / volatility_naive
print(sharpe_naive)