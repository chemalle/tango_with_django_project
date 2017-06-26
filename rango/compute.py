#!/usr/bin/python
# -*- coding: utf-8 -*-

# sharpe.py

from __future__ import print_function

import datetime
import numpy as np
import pandas as pd
#import pandas.io.data as web
import quandl


def annualised_sharpe(returns, N=252):
    """
    Calculate the annualised Sharpe ratio of a returns stream
    based on a number of trading periods, N. N defaults to 252,
    which then assumes a stream of daily returns.

    The function assumes that the returns are the excess of
    those compared to a benchmark.
    """
    return np.sqrt(N) * returns.mean() / returns.std()


def compute(r):
    """
    Calculates the annualised Sharpe ratio based on the daily
    returns of an equity ticker symbol listed in Google Finance.

    The dates have been hardcoded here for brevity.
    """
    pdf = quandl.get('wiki/'+r, authtoken="oAe9Zos9MifP13eC9yRM",rows=252)

    # Use the percentage change method to easily calculate daily returns
    pdf['daily_ret'] = pdf['Close'].pct_change()

    # Assume an average annual risk-free rate over the period of 5%
    pdf['excess_daily_ret'] = pdf['daily_ret'] - 0.05/252

    # Return the annualised Sharpe ratio based on the excess daily returns
    return annualised_sharpe(pdf['excess_daily_ret'])