import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px

st.write("Tweet Analysis")

st.sidebar.title('Upload Data')
uploaded_file = st.sidebar.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S+00:00')

    df.set_index('date', inplace=True)

    tweets_per_hour = df.resample('H').size()
    tweets_per_day = df.resample('D').size()

    fig_hour = px.line(tweets_per_hour, title='Number of Tweets per Hour')
    st.plotly_chart(fig_hour, use_container_width=True)

    fig_day = px.line(tweets_per_day, title='Number of Tweets per Day')
    st.plotly_chart(fig_day, use_container_width=True)
else:
    st.sidebar.info('Please upload a CSV file.')