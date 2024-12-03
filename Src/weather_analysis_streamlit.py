import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Page Config
st.set_page_config(page_title="Weather Data Analysis", layout="wide")

# Header Section
st.markdown(
    """
    <style>
    .title {
        font-size: 45px;
        color: #4CAF50;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-size: 18px;
        color: #808080;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="title">🌦️ Weather Data Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Analyze temperature, humidity, and rainfall trends effortlessly!</div>', unsafe_allow_html=True)

# Upload Section
st.write("### Upload CSV File")
st.info("💡 *Please upload a CSV file (max size: 200MB)*.")

# File Upload
uploaded_file = st.file_uploader("Drag and drop your file or click Browse files", type=["csv"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")
    st.write("### File Preview:")
    try:
        weather_data = pd.read_csv(uploaded_file)
        st.dataframe(weather_data.head())  # Display the first few rows of the uploaded file
        
        # Sidebar for region selection
        st.sidebar.title("Weather Data Analysis")
        region = st.sidebar.selectbox('Select Region:', weather_data['location_name'].unique())
        
        # Main layout
        st.title('Weather Pattern Analysis')
        col1, col2 = st.columns(2)
        
        with col1:
            # Function to create line charts for various parameters
            def create_line_chart(region_data, parameter, title):
                fig = px.line(region_data, x='last_updated_epoch', y=parameter, title=title)
                st.plotly_chart(fig)
            
            create_line_chart(weather_data[weather_data['location_name'] == region], 'temperature_celsius', f'Temperature Trends for {region}')
            create_line_chart(weather_data[weather_data['location_name'] == region], 'humidity', f'Humidity Trends for {region}')
        
        with col2:
            create_line_chart(weather_data[weather_data['location_name'] == region], 'precip_mm', f'Rainfall Trends for {region}')
            create_line_chart(weather_data[weather_data['location_name'] == region], 'wind_mph', f'Wind Speed Trends for {region}')
        
        st.write("### Additional Parameters")
        st.write(f"Pressure: {weather_data[weather_data['location_name'] == region]['pressure_mb'].mean():.2f} mb")
        st.write(f"Visibility: {weather_data[weather_data['location_name'] == region]['visibility_km'].mean():.2f} km")
    except Exception as e:
        st.error(f"Error reading the file: {e}")
else:
    st.write("Please upload a CSV file to proceed.")

# Footer Section
st.markdown(
    """
    <hr>
    <footer style="text-align:center; font-size: 12px; color: #808080;">
        Made by Parthrajsinh
    </footer>
    """, unsafe_allow_html=True)
