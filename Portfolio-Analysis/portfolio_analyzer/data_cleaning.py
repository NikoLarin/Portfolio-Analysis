import pandas as pd

DATE_CANDIDATES = [
    "Date", "Transaction Date", "Time", "Created At", "Date/Time", 
    "timestamp", "Date Time", "Trans Date", "Trade Date", "Settlement Date",
    "Posted Date", "Effective Date", "Activity Date"
]

BALANCE_CANDIDATES = [
    "Balance", "Net Liquidation", "Portfolio Value", "Account Value", 
    "Equity", "Amount", "Total Value", "Portfolio Equity", "Net Worth",
    "Market Value", "Cash + Securities", "Total Equity", "Buying Power",
    "Net Asset Value", "Account Equity", "Cash Balance", "Securities Value"
]

def clean_balance_data(file_path, start_date=None):
    """
    Clean balance data from any brokerage CSV.
    start_date: Only include data ON or AFTER this date (YYYY-MM-DD)
    """
    df = pd.read_csv(file_path)
    
    # Auto-detect columns
    date_col = next((col for col in df.columns 
                     if any(cand.lower() in col.lower() for cand in DATE_CANDIDATES)), None)
    
    balance_col = next((col for col in df.columns 
                        if any(cand.lower() in col.lower() for cand in BALANCE_CANDIDATES)), None)
    
    if not date_col or not balance_col:
        raise ValueError(f"Could not detect columns in {file_path}\nAvailable: {list(df.columns)}")
    
    # Rename
    df = df.rename(columns={date_col: 'Date', balance_col: 'Balance'})
    
    # Clean Date
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    
    # Clean Balance
    if df['Balance'].dtype == 'object':
        df['Balance'] = df['Balance'].astype(str).str.replace(r'[\$,]', '', regex=True).astype(float)
    
    # Sort
    df = df.sort_values('Date').reset_index(drop=True)
    
    # Filter from start_date onward
    if start_date:
        start_date = pd.to_datetime(start_date)
        df = df[df['Date'] >= start_date]
    
    return df[['Date', 'Balance']][::-1]

#print(BROKER_CONFIG["Schwab"]["balance"])

'''
def clean_transaction_data(data):
    df = pd.read_csv(data, index_col="Date")

    df = df.drop(columns=["Fees & Comm"])
    df = df.dropna(subset=["Quantity", "Price", "Amount"])
    df["Amount"] = df["Amount"].str.replace("$", "", regex=False)
    df["Amount"] = df["Amount"].str.replace("-", "", regex=False)
    
    return df
'''
