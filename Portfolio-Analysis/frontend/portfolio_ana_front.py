import streamlit as st
import pandas as pd
import sys
from pathlib import Path


# Add parent directory to path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import *

st.set_page_config(page_title="Portfolio Analyzer", layout="wide")

st.title("Portfolio Analyzer", text_alignment="left", )
st.subheader(f"Portfolio Value: :green[${portfolio_value}]", text_alignment="left")

balance_chart_data = balance_data
balance_chart_data = balance_data.iloc[::-1]
balance_chart_data = balance_chart_data.drop(columns=["Return"]) 
balance_chart_data = balance_chart_data.reset_index()
balance_chart_data = balance_chart_data.drop(balance_chart_data.index[0])

pnl_chart_data = balance_chart_data
pnl_chart_data = pnl_chart_data["Amount"] - 7800

st.header("Metrics", divider=True, text_alignment= "center")


col1, col2, col3, col4 = st.columns(4)

with col1:
    #st.header("Daily")
    st.metric("Total Return", f'{profit_loss[1]}%')

with col2:
    #st.header("Monthly")
    st.metric("Annual Volatility", f'{portfolio_volatility[2]:.1%}')

with col3:
    #st.header("Annual")
    st.metric("Sharpe Ratio", f'{portfolio_sharpe}')

with col4:
    st.metric("Max Drawdown", f'{max_drawdown}%')

tab1, tab2, tab3 = st.tabs(["📊 Performance", "📉 Risk Analysis", "📈 Visuals"])

with tab1:
    st.subheader("Balance")
    st.line_chart(balance_chart_data, y="Amount", x_label="Day", )
    st.subheader(":green[Profit] & :red[Loss]")
    st.line_chart(pnl_chart_data, y="Amount", x_label="Day", color="#C4ABDB")


with tab2:
    pass
with tab3:
    pass
