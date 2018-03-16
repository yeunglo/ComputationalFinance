from itertools import combinations

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
stocks = ['SDR.L', 'NMC.L', 'CPG.L', 'BT', 'SHP.L', 'PRU.L', 'SKY.L', 'BNZL.L', 'STJ.L', 'TSCO.L', 'EZJ.L', 'GFS.L', 'CCL.L', 'EXPN.L', 'RSA.L', 'SMIN.L', 'SSE.L', 'CNA.L', 'TUI.L', 'CCH.L', 'RTO.L', 'VOD.L', 'BATS.L', 'AHT.L', 'PPB.L', 'BRBY.L', 'ANTO.L', 'DLG.L', 'UU.L', 'BCS']
stocks_c = []
for c in combinations(stocks, 3):
    c = list(c)
    stocks_c.append(c)

print(stocks_c)
print(len(stocks_c))
print(stocks_c[0])
port_sharpe = {}
sharpe_portfolio_prev = pd.read_csv('./stocks30.csv', index_col = 'Date')
sharpe_portfolio_prev = sharpe_portfolio_prev.iloc[1,:]

for i in range(len(stocks_c)):
    set_three = data.loc[:,stocks_c[i]]
    # print(set_three)

    # calculate daily and annual returns of the stocks
    returns_daily = set_three.pct_change()
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
    port_sharpe = {4059: {'Returns': {29: 0.00010815790042369416}, 'Volatility': {29: 0.01236368212747541}, 'Sharpe Ratio': {29: 0.008748033094715236}, 'MV Model': {29: -0.006073683163314011}, 'DLG.L Weight': {29: 0.8376836972148671}, 'UU.L Weight': {29: 0.05674803103228276}, 'BCS Weight': {29: 0.1055682717528501}}}

    # set the number of combinations for imaginary portfolios
    num_assets = 3
    num_portfolios = 1000

    # populate the empty lists with each portfolios returns,risk and weights
    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        # print('w1:', weights)
        weights /= np.sum(weights)
        # print('w2:', weights)
        returns_three = np.dot(weights, returns_one)
        volatility = np.sqrt(np.dot(weights.T, np.dot(covariance, weights)))
        sharpe = returns_three / volatility
        mv = returns_three - np.dot(0.5, volatility)
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
    for counter, symbol in enumerate(stocks_c[i]):
        portfolio[symbol + ' Weight'] = [Weight[counter] for Weight in stock_weights]

    # make a nice dataframe of the extended dictionary
    portfolios = pd.DataFrame(portfolio)

    # print(portfolios)

    # get better labels for desired arrangement of columns
    column_order = ['Returns', 'Volatility', 'Sharpe Ratio', 'MV Model'] + [stock + ' Weight' for stock in
                                                                            stocks_c[i]]

    # reorder dataframe columns
    portfolios = portfolios[column_order]
    # print(portfolios)

    # find min Volatility & max sharpe & max MV values in the dataframe (df)
    min_volatility = portfolios['Volatility'].min()
    max_sharpe = portfolios['Sharpe Ratio'].max()
    max_mv = portfolios['MV Model'].max()

    # use the min, max values to locate and create the three special portfolios
    sharpe_portfolio = portfolios.loc[portfolios['Sharpe Ratio'] == max_sharpe]
    min_variance_port = portfolios.loc[portfolios['Volatility'] == min_volatility]
    mv_portfolio = portfolios.loc[portfolios['MV Model'] == max_mv]
    # sharpe_portfolio_dict = sharpe_portfolio.to_dict(orient='dict')
    sharpe_portfolio.to_csv('port_detail.csv', mode='a', header=True, index=True)
    sharpe_portfolio.to_csv('port.csv', mode='a', header=False)



    # print(port_sharpe)


    # print the details of the 2 special portfolios
    # print(min_variance_port.T)
    # print(sharpe_portfolio.T)
    # print(mv_portfolio.T)
    # print(pd.merge(min_variance_port.T, sharpe_portfolio.T,left_index=True, right_index=True, how='inner'))
    # print(pd.merge((pd.merge(min_variance_port.T, sharpe_portfolio.T, left_index=True, right_index=True, how='inner')),
    #              mv_portfolio.T, left_index=True, right_index=True, how='inner'))
    # find max(expected return - risk)
print(port_sharpe)
