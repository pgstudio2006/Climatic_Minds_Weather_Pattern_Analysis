import pandas as pd
import time
import plotly.express as px
import streamlit as st

# Function to ingest data
def ingest_data(file_path):
    return pd.read_csv(file_path)

# Function to clean data
def clean_data(df):
    df.dropna(inplace=True)
    return df

# Function to transform data
def transform_data(df):
    df['temperature_fahrenheit'] = df['temperature_celsius'] * 9/5 + 32
    return df

# Function to analyze data
def analyze_data(df):
    analysis = {
        'avg_temp': df['temperature_celsius'].mean(),
        'avg_humidity': df['humidity'].mean(),
        'total_rainfall': df['precip_mm'].sum()
    }
    return analysis

# Function to visualize data
def visualize_data(df):
    fig = px.line(df, x='last_updated_epoch', y='temperature_celsius', title='Temperature Trends')
    st.plotly_chart(fig)

# Main pipeline function
def run_pipeline(file_path):
    while True:
        df = ingest_data(file_path)
        df = clean_data(df)
        df = transform_data(df)
        analysis = analyze_data(df)
        visualize_data(df)
        print("Analysis:", analysis)
        time.sleep(3600)  # Update every hour

# Example usage
# run_pipeline('C:/Users/Riddhi/Desktop/Data/GlobalWeatherRepository.csv')
