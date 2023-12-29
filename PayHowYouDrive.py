import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "OBD2Dataset.csv"
df = pd.read_csv(file_path)

# Set page configuration to wide layout
st.set_page_config(layout='wide')

# Page Title
st.title("Pay How You Drive")

# Selectbox for DriverId in the top left corner
st.sidebar.title("Select DriverId")
selected_driver = st.sidebar.selectbox("Choose DriverId:", df['DriverId'].unique())

# Basic statistics (you can hide it if not needed)
st.sidebar.header("Basic Statistics")
st.sidebar.write("Basic Statistics:")
st.sidebar.write(df[['SPEED','EngineSpeed', 'MAF']].describe())

# Create two columns for the map and speed diagram
col1, col2 = st.columns(2)

# Scatter plot for Latitude and Longitude (Map)
with col1:
    st.header(f"Places visited by DriverId: {selected_driver}")
    fig_map = px.scatter_mapbox(
        df[df['DriverId'] == selected_driver],
        lat='Latitude',
        lon='Longitude',
        color='DriverId',
        size='EngineSpeed',
        hover_name='DriverId',
        hover_data=['SPEED', 'EngineSpeed'],
        mapbox_style='open-street-map',
        title=f'Scatter Plot for DriverId: {selected_driver}'
    )
    st.plotly_chart(fig_map)

# Scatter plot for SPEED distribution over time
with col2:
    st.header(f"SPEED Distribution for DriverId: {selected_driver}")
    fig_speed_scatter = px.scatter(
        df[df['DriverId'] == selected_driver],
        x='time',
        y='SPEED',
        title='SPEED Distribution over Time',
        labels={'SPEED': 'Speed'},
        color='DriverId',
        size='SPEED',
        hover_data=['SPEED', 'EngineSpeed']
    )
    st.plotly_chart(fig_speed_scatter)

# Box plot for Fuel Type below the speed diagram
# Bar chart for Fuel Type
st.header(f"Fuel Type Distribution for DriverId: {selected_driver}")
fig_fuel_type_bar = px.histogram(df[df['DriverId'] == selected_driver], x='FuelType', title='Fuel Type Distribution', nbins=2)
fig_fuel_type_bar.update_layout(barmode='overlay', bargap=0.1)
st.plotly_chart(fig_fuel_type_bar)


# Display the dataset (you can hide it if not needed)
st.header("OBD2 Dataset")
st.write("Here is the loaded dataset:")
st.write(df)
