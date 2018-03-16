import csv
import pandas as pd
# import quandl
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot
# pyplot.use('TkAgg')
# import os
from cvxpy import *

# best = pd.read_csv('./best.csv')
# weights = best.ix[0,['SDR.L Weight', 'NMC.L Weight', 'CPG.L Weight']]
# weights = np.array(weights)
# print(weights)


data = pd.read_csv('./stocks30.csv', index_col = 'Date')
# print(data)
trainset = data.iloc[0:378]
testset = data.iloc[378:756]


# trainset_three = trainset.loc[:,['SDR.L', 'NMC.L', 'CPG.L']]
# testset_three = testset.loc[:,['SDR.L', 'NMC.L', 'CPG.L']]
# print(trainset_three)
# print(testset_three)

# calculate daily and annual returns of the stocks
train_returns_daily = data.pct_change()
returns_one = train_returns_daily.mean()
# print(trainset.pct_change())
# print('returns:',train_returns_daily)

test_returns_daily = data.pct_change()
print(test_returns_daily)
test_returns_daily = np.array(test_returns_daily[1:].T)
# print(test_returns_daily)
# get daily and covariance of returns of the stock
covariance = train_returns_daily.cov()
covariance.index.name = 'stock'
print('covariance:',covariance)

ftse = pd.read_csv('./ftse_data.csv', index_col = 'Date')
ftse_close = ftse.ix[1:,['Close']]
print(ftse_close)
ftse_close = np.array(ftse_close)

# returns = np.dot(weights.T, returns_one)
# print(returns)
taw = 0.0005

# Problem data.
m = 30
n = 756
np.random.seed(1)
A = test_returns_daily.T
b = np.random.randn(m)

# Construct the problem.
x = Variable(m,1)
objective = Minimize(norm(ftse_close - (A*x), 2) + norm((taw*x), 1))
constraints = [x >= 0 ]
prob = Problem(objective, constraints)

# The optimal objective is returned by prob.solve().
result = prob.solve()
# The optimal value for x is stored in x.value.
print(x.value)

# The optimal Lagrange multiplier for a constraint
# is stored in constraint.dual_value.
print(constraints[0].dual_value)

test_weights = []
test_weights_adjust = []
for j in range(len(x.value)):
    test_weights.append(x.value[j,0])
test_weights = np.array(test_weights)
for q in range(len(test_weights)):
    test_weights /= np.sum(test_weights)

print('weights')
print(test_weights)
weights = pd.DataFrame(test_weights)

# weights = pd.concat([covariance, weights], axis=1)
print(weights)
stocks = ['SDR.L', 'NMC.L', 'CPG.L', 'BT', 'SHP.L', 'PRU.L', 'SKY.L', 'BNZL.L', 'STJ.L', 'TSCO.L', 'EZJ.L', 'GFS.L', 'CCL.L', 'EXPN.L', 'RSA.L', 'SMIN.L', 'SSE.L', 'CNA.L', 'TUI.L', 'CCH.L', 'RTO.L', 'VOD.L', 'BATS.L', 'AHT.L', 'PPB.L', 'BRBY.L', 'ANTO.L', 'DLG.L', 'UU.L', 'BCS']
stocks = pd.DataFrame(stocks)
weights = pd.concat([stocks, weights], axis=1)
weights.columns = ['a', 'b']
weights=weights.sort_values(by='b',ascending=False)

print(weights)


print(sum(weights[0:5,['b']]))


