# Portfolio Analysis Tool

Python tool for analyzing **Schwab brokerage** statements and calculating portfolio performance metrics

![Language Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

# 🟢Table of Contents 
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Metrics](#metrics)

#  🔵Features
- Clean Schwab balance and transaction CSV data
- Select custom reporting period for your data
- Calculate multiple financial performance indicators
- Generate _easy to read_ summary
- Interactive UI

<img width="387" height="122" alt="image" src="https://github.com/user-attachments/assets/8c1ee653-29cc-4729-9023-284d7cd2f765" />
<img width="1807" height="799" alt="image" src="https://github.com/user-attachments/assets/a6f73e00-edfc-40d3-80f2-05cae8632f2c" />


#  🟡Installation


## 1. Clone the repo
-```git clone https://github.com/NikoLarin/Portfolio-Analysis.git```

-```cd Portfolio-Analysis```

## 2. Install dependencies
```pip install -r requirements.txt```   

#  🟠Usage
1. Enter your data in main.py
```
BALANCE_PATH = "BALANCES_DATA_PATH"
TRANSACTION_PATH = "TRANSACTIONS_DATA_PATH" 
```
2.  Change your starting data in main.py, ex: "5/7/26" for May 7th, 2026
```
balance_data = clean_balance_data(BALANCE_PATH, "STARTING_DATE")
```

4. Run the program
```
python main.py
```

6. Output
```
Reporting Period        :   5/7/2026 ----> 6/26/2026
Portfolio Value         :   $11000
Your P&L is             :   $1000 | 10%
All time trading volume :   $1178612
Your Sharpe Ratio is    :   1
Dail|Mont|Ann Vol       :   [0.005, 0.05, 0.12]
```

#  🟣Metrics
- Portfolio value
- Profit/Loss in dollars and percentage
- All time trading volume
- Sharpe ratio
- Daily, monthly, and annual standard deviation
