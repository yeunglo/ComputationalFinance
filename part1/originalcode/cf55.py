import csv
import pandas as pd
# import quandl
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot
# pyplot.use('TkAgg')
# import os
from cvxpy import *

best = pd.read_csv('./best.csv')
weights = best.ix[0,['SDR.L Weight', 'NMC.L Weight', 'CPG.L Weight']]
weights = np.array(weights)
print(weights)


data = pd.read_csv('./stocks30.csv', index_col = 'Date')
# print(data)
trainset = data.iloc[0:378]
testset = data.iloc[378:756]


trainset_three = trainset.loc[:,['SDR.L', 'NMC.L', 'CPG.L']]
testset_three = testset.loc[:,['SDR.L', 'NMC.L', 'CPG.L']]
# print(trainset_three)
# print(testset_three)

# calculate daily and annual returns of the stocks
train_returns_daily = trainset_three.pct_change()
returns_one = train_returns_daily.mean()
# print(trainset.pct_change())
# print('returns:',train_returns_daily)

test_returns_daily = testset_three.pct_change()
# print(test_returns_daily)
test_returns_daily = np.array(test_returns_daily[1:].T)
# print(test_returns_daily)
# get daily and covariance of returns of the stock
covariance = train_returns_daily.cov()
covariance = np.array(covariance)
print('covariance:',covariance)
covariance_inv = np.linalg.inv(covariance)
print('covariance_inv:',covariance_inv)

returns = np.dot(weights.T, returns_one)
# print(returns)
taw = 0.9

# Problem data.
m = 3
n = 378
np.random.seed(1)
# A =
b = np.random.randn(m)

# Construct the problem.
x = Variable(m,1)

objective = Maximize( -0.5 * (covariance_inv * (returns_one + x)).T * ( returns_one + x) )
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


print(test_weights)
