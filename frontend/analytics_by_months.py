import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")
    monthly_summary = response.json()

    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    df = pd.DataFrame(monthly_summary)
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month",
        "total": "Total"
    }, inplace=True)

    df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)

    df_sorted = df.sort_values(by="Month Number")
    df_sorted = df_sorted.set_index("Month Number")

    st.title("Expense Breakdown By Months")

    st.bar_chart(df_sorted.set_index('Month')["Total"], use_container_width=True)

    df_sorted_table = df_sorted.copy()
    df_sorted_table.index.name = ""
    df_sorted_table["Total"] = df_sorted_table["Total"].map("{:.2f}".format)

    st.table(df_sorted_table.sort_index())
