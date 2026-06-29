import pandas as pd
import numpy as np

def get_volatility(balance_data): #Calculate portfolio vol with daily change
    balance_data["Return"] = balance_data["Balance"].pct_change()
    daily_returns = balance_data['Return'].dropna()[:-1]

    daily_volatility = np.std(daily_returns)
    monthly_volatility = np.std(daily_returns) * np.sqrt(21)
    annual_volatility = np.std(daily_returns) * np.sqrt(252)

    volatilities = [daily_volatility, monthly_volatility, annual_volatility]
    
    return [round(float(x), 2) for x in volatilities]

def get_sharpe(balance_data, risk_free_rate = .04):
    balance_data["Return"] = balance_data["Balance"].pct_change()
    daily_returns = balance_data['Return'].dropna()[:-1]
    
    mean_daily_return = daily_returns.mean()
    annual_return = float(mean_daily_return * 252)
    
    annual_volatility = np.std(daily_returns) * np.sqrt(252)

    sharpe = round(float(annual_return - risk_free_rate) / annual_volatility, 2)

    return sharpe

def get_pnl(balance_data):
    start = balance_data["Balance"].iloc[0]
    end = balance_data["Balance"].iloc[-2]
    pct_change = round((start - end) / end * 100, 2)

    return [round(start - end), float(pct_change)]

def get_transaction_volume(transaction_data):
    transaction_volume = transaction_data["Balance"]
    transaction_volume = transaction_volume.astype(float)
    transaction_volume = transaction_volume.sum()
  
    return transaction_volume

def get_max_drawdown(balance_data):
    balance = balance_data.drop(columns=["Return"]) # create numpy array
    balance = balance_data.drop(balance_data.index[-1])
    balance = balance.iloc[::-1]

    balance["Running_Max"] = balance["Balance"].cummax() # create a running max column

    balance["Drawdown"] = (balance["Balance"] - balance['Running_Max']) / balance['Running_Max']

    max_drawdown = balance['Drawdown'].min()

    
    max_drawdown_pct = max_drawdown * 100

    return max_drawdown_pct

