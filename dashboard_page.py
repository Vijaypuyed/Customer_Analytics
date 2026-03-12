# dashboard_page.py

import streamlit as st
import pandas as pd

def show_dashboard():

    # --- Sample Data ---
    customers = pd.DataFrame({
        "customer_id":[1,2,3,4],
        "name":["Rahul","Amit","John","Sara"],
        "country":["India","India","USA","UK"]
    })

    subscriptions = pd.DataFrame({
        "customer_id":[1,2,3,4],
        "plan":["Pro","Basic","Enterprise","Pro"],
        "status":["Active","Cancelled","Active","Active"]
    })

    payments = pd.DataFrame({
        "customer_id":[1,2,3,4],
        "amount":[500,200,800,400],
        "month":["Jan","Feb","Jan","Mar"]
    })

    # --- Metrics ---
    total_customers = customers.shape[0]
    active_users = subscriptions[subscriptions["status"]=="Active"].shape[0]
    cancelled = subscriptions[subscriptions["status"]=="Cancelled"].shape[0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", total_customers)
    col2.metric("Active Customers", active_users)
    col3.metric("Cancelled Customers", cancelled)

    st.subheader("Revenue by Month")
    revenue = payments.groupby("month")["amount"].sum()
    st.bar_chart(revenue)

    st.subheader("Customer Data")
    st.dataframe(customers)