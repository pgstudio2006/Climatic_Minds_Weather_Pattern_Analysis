# Climatic_Minds_Weather_Pattern_Analysis

## Group Members
- Parthrajsinh Gohil KU2407U067
- Isha Dholariya KU2407U082
- Himilkumar Maheta KU2407U080
- Het Patel KU2407U076

## Objective of the Project
The objective of this project is to analyze weather patterns by visualizing temperature, humidity, and rainfall trends across multiple regions. This tool provides insights into weather behavior and enables comparisons between different regions. The project aims to develop a tool that helps users understand and analyze weather data over time. By integrating interactive visualizations and multiple analysis modes, the tool allows for a deeper understanding of climatic dynamics and regional weather behavior.

## Tools and Libraries Used
- **Programming Language**: Python
- **Libraries**:
  - **Pandas**: For data manipulation and analysis.
  - **Plotly**: For creating interactive visualizations.
  - **Streamlit**: For building the web application interface.

## Data Source(s)
The weather dataset is sourced from a CSV file named `GlobalWeatherRepository.csv`.
The dataset contains columns like:
- `location_name`: Location name
- `temperature_celsius`: Temperature in Celsius
- `humidity`: Humidity percentage
- `precip_mm`: Precipitation in millimeters

## Execution Steps
### Prepare the Environment:
- Ensure Python 3.x is installed.
- Install required libraries using:
  ```bash
  pip install pandas plotly streamlit
  ```

### Place the Data File:
- Save your `GlobalWeatherRepository.csv` file in the specified directory.

### Run the Application:
- Execute the Streamlit app:
  ```bash
  streamlit run weather_analysis_streamlit.py
  ```

### Interact with the Application:
- Upload the CSV file.
- Select a region to analyze.
- View interactive visualizations of weather trends.

## Summary of Results
The application provides:
- Trend analysis for temperature, humidity, and rainfall.
- Interactive visualizations for selected regions.

## Challenges Faced
- **Data Quality**: Ensuring the dataset was clean and consistent.
- **Visualization**: Creating interactive and informative visualizations.
- **User Interface**: Designing an intuitive and user-friendly interface.

This project aims to provide users with a comprehensive tool to explore and analyze weather data, offering valuable insights into climatic trends and behaviors across different regions.
