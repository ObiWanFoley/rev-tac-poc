# Import Modules
import streamlit as st
import pandas as pd
import numpy as np
import plotly as plt
import plotly.graph_objects as go
import plotly.express as px


# -----------------------------------------------------------
# Initial Work in This Section
# -----------------------------------------------------------
df = pd.read_csv('revenue.csv')
brands = df.Brand.unique()
product_lines = list(df['Product Line'].unique())
metrics = list(df.columns[3:])
cols = list(product_lines[4:7])


metric_selector = st.selectbox(
    'Select a metric to view',
    options=metrics
)

product_selector = st.multiselect(
    'Select Product Lines to View',
    options=product_lines,
    default=cols)

df_graph = df[df['Product Line'].isin(product_selector)]



# -----------------------------------------------------------
# Streamlit App in This Section
# -----------------------------------------------------------

'''
# IMH Revenue Data - POC
'''

# Create figure
graph = px.line(df_graph, x='Payment Date', y=metric_selector, color='Product Line')

# Add range slider
graph.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)
graph

