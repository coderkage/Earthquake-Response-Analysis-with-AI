import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import matplotlib.pyplot as plt
import plotly.express as px
import webbrowser
import numpy as np

def color_marker(frequency, min_frequency, max_frequency):
    normalized_freq = (frequency - min_frequency) / (max_frequency - min_frequency)
    color = (int(normalized_freq * 200), int((1 - normalized_freq) * 128), 0)  # Green to Red spectrum
    return '#%02x%02x%02x' % color

@st.cache_data
def load_map_data(file_path):
    return pd.read_csv(file_path)

# @st.cache_data
# def load_pie_data(file_path):
#     return pd.read_csv(file_path)

def plot_locations(df, open_in_new_tab):
    st.title("Locations Visualization")
    
    min_frequency = df['Frequency'].min()
    max_frequency = df['Frequency'].max()

    max_freq_location = df.loc[df['Frequency'].idxmax()]
    map_center = (max_freq_location['Latitude'], max_freq_location['Longitude'])

    my_map = folium.Map(location=map_center, zoom_start=6)
    mean_frequency = df['Frequency'].mean()
    std_frequency = df['Frequency'].std()
    
    for idx, row in df.iterrows():
        location = (row['Latitude'], row['Longitude'])
        marker_size = (row['Frequency'] - mean_frequency) / std_frequency

        # Ensure marker size is non-negative and scaled appropriately
        marker_size = 2* max(3, marker_size * 1)  # Adjust scaling for visibility

        folium.CircleMarker(
            location=location,
            radius=marker_size,
            color=color_marker(row['Frequency'], min_frequency, max_frequency),
            fill=True,
            fill_color=color_marker(row['Frequency'], min_frequency, max_frequency),
            fill_opacity=0.5,
            popup=f"<b>{row['Location']}</b><br>Frequency: {row['Frequency']}",
        ).add_to(my_map)

    # Render map
    folium_static(my_map)

    if open_in_new_tab:
        map_html = my_map.get_root().render()
        with open("map.html", "w") as f:
            f.write(map_html)
        webbrowser.open_new_tab("map.html")

    if open_in_new_tab:
        map_html = my_map.get_root().render()
        with open("map.html", "w") as f:
            f.write(map_html)
        webbrowser.open_new_tab("map.html")

def generate_3d_pie_chart(df):
    st.title("Location Distribution")
    location_counts = df['Location'].value_counts()

    fig = px.pie(location_counts, values=location_counts.values, names=location_counts.index, title='Location Distribution')
    fig.update_traces(textinfo='percent+label', pull=[0.1]*len(location_counts))

    st.plotly_chart(fig)

# Streamlit UI
st.set_page_config(layout="wide")
st.title("Location Visualization App")

uploaded_map_file = st.file_uploader("Upload CSV file for Map Visualization", type=["csv"])

    # File uploader for pie chart
# uploaded_pie_file = st.file_uploader("Upload CSV file for Pie Chart", type=["csv"])

if uploaded_map_file is not None:
        # Load data for map visualization
    map_df = load_map_data(uploaded_map_file)
        # Plot locations
    open_in_new_tab = st.checkbox("Open map in new tab (fullscreen)")
    plot_locations(map_df, open_in_new_tab)

        # Load data for pie chart
    # pie_df = load_pie_data(uploaded_pie_file)
        # Generate pie chart
    # generate_3d_pie_chart(pie_df)