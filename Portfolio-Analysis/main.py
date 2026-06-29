import pandas as pd
import numpy as np
from portfolio_analyzer.data_cleaning import clean_balance_data
from portfolio_analyzer.metrics_calculator import * 

BALANCE_PATH = "/Users/nikolarin/Downloads/Custodial Brokerage_XXXX300_Balances_20260626-141945.CSV"

balance_data = clean_balance_data(BALANCE_PATH, "2026-05-08")


reporting_period = f'{balance_data.index[-1]} ----> {balance_data.index[0]}'
portfolio_value = balance_data["Balance"].iloc[0]
portfolio_sharpe = get_sharpe(balance_data)
portfolio_volatility = get_volatility(balance_data)
profit_loss = get_pnl(balance_data)
max_drawdown = round(get_max_drawdown(balance_data),2)

print(f'Reporting Period        :   {reporting_period}\n'
      f'Portfolio Value         :   ${portfolio_value}\n'
      f'Your P&L is             :   ${profit_loss[0]} | {profit_loss[1]}%\n'
      f'Sharpe Ratio            :   {portfolio_sharpe}\n'
      f'Dail|Mont|Ann Vol       :   {portfolio_volatility}\n'
      f'Max drawdown            :   {max_drawdown}%'
)


