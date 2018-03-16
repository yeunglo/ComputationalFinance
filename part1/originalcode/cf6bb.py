import csv
import pandas as pd
# import quandl
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import pyplot
# pyplot.use('TkAgg')
# import os

port = pd.read_csv('./port.csv')
port_detail = pd.read_csv('./port_detail.csv')
# print(port)
# print(port_detail)

# find min Volatility & max sharpe & max MV values in the dataframe (df)


max_sharpe = port['Sharpe Ratio'].max()
min_sharpe = port['Sharpe Ratio'].min()

# use the min, max values to locate and create the three special portfolios
sharpe_portfolio = port.loc[port['Sharpe Ratio'] == max_sharpe]
nonsharpe_portfolio = port.loc[port['Sharpe Ratio'] == min_sharpe]

print(sharpe_portfolio)
print(nonsharpe_portfolio)