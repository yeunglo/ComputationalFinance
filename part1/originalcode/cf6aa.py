# import csv
import pandas as pd
# import quandl
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./stocks30.csv', index_col = 'Date')

# calculate daily and annual returns of the stocks
returns_daily = data.pct_change()
returns_ones = returns_daily.mean()
returns_ones = pd.DataFrame(returns_ones)
returns_one = np.array(returns_ones)
print('returns:',returns_ones)

# get daily and covariance of returns of the stock
covariance = returns_daily.cov()
covariance = np.diag(covariance)
covariances = pd.DataFrame(covariance)
print('covariance:',covariance)
# print('covariance:',covariance(0,0))

weights = np.ones(30)
volatility = np.sqrt(covariance)
print('volatility:',volatility)

sharpe_ratio = returns_one / volatility
print('sharpe_ratio:',sharpe_ratio)
stocks = ['SDR.L', 'NMC.L', 'CPG.L', 'BT', 'SHP.L', 'PRU.L', 'SKY.L', 'BNZL.L', 'STJ.L', 'TSCO.L', 'EZJ.L', 'GFS.L', 'CCL.L', 'EXPN.L', 'RSA.L', 'SMIN.L', 'SSE.L', 'CNA.L', 'TUI.L', 'CCH.L', 'RTO.L', 'VOD.L', 'BATS.L', 'AHT.L', 'PPB.L', 'BRBY.L', 'ANTO.L', 'DLG.L', 'UU.L', 'BCS']

sharpe_ratio = pd.DataFrame(sharpe_ratio)
# sharpe_ratio.index.name = 'Stock'
stocks = pd.DataFrame(stocks)
# stocks.index.name = 'Stock'

sharpe = pd.merge(stocks ,sharpe_ratio, left_index=True, right_index=True, how='outer')
sharpe.index.name = 'no'
print(sharpe)
best_num = []
best = {}

stocks = ['SDR.L', 'NMC.L', 'CPG.L', 'BT', 'SHP.L', 'PRU.L', 'SKY.L', 'BNZL.L', 'STJ.L', 'TSCO.L', 'EZJ.L', 'GFS.L', 'CCL.L', 'EXPN.L', 'RSA.L', 'SMIN.L', 'SSE.L', 'CNA.L', 'TUI.L', 'CCH.L', 'RTO.L', 'VOD.L', 'BATS.L', 'AHT.L', 'PPB.L', 'BRBY.L', 'ANTO.L', 'DLG.L', 'UU.L', 'BCS']
sharpe_ratio = pd.DataFrame(sharpe_ratio)
returns = pd.merge(stocks ,returns_ones, left_index=True, right_index=True, how='outer')
returns.index.name = 'no'
print(returns)
best_num_r = []
best_r = {}




for i in range(6):
    max_sharpe = sharpe['0_y'].max()
    max_return = returns['0_y'].max()
    best_one = sharpe[(sharpe['0_y'] == max_sharpe)].index.tolist()
    best_one_r = returns[(returns['0_y'] == max_return)].index.tolist()
    best_num.append(best_one[0])
    best_num_r.append(best_one_r[0])
    print('stock',sharpe.at[best_one[0], '0_y'])
    value = [sharpe.at[best_one[0], '0_x']]
    value_r = [returns.at[best_one_r[0], '0_x']]
    print(value)
    value.extend([sharpe.at[best_one[0], '0_y']])
    value_r.extend([returns.at[best_one_r[0], '0_y']])
    best[i] = value
    best_r[i] = value_r
    sharpe = sharpe.drop([best_one[0]])
    returns = returns.drop([best_one_r[0]])


best = pd.DataFrame(best)
best_r = pd.DataFrame(best_r)
print(max_sharpe)
print(best)
print(best_r)