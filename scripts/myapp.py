import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit application title
st.title('Environmental Data Dashboard')

# Upload CSV file via Streamlit
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load the uploaded data
    df = pd.read_csv(uploaded_file)
    st.write(df.head())  # Display the first few rows of the dataset

    # Display data summary
    st.header('Data Summary')
    st.write(df.describe())

    # Plot Correlation Matrix
    st.header('Correlation Matrix')
    numeric_df = df.select_dtypes(include=['float64', 'int64'])  # Select only numeric columns
    if not numeric_df.empty:
        corr_matrix = numeric_df.corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=ax, vmin=-1, vmax=1)
        ax.set_title('Correlation Matrix')
        st.pyplot(fig)
    else:
        st.write("No numeric data available for correlation matrix.")

    # Plot Time Series Data (if 'Timestamp' column is present)
    st.header('Time Series Plots')
    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        df.set_index('Timestamp', inplace=True)

        st.subheader('GHI, DNI, DHI, and Tamb Over Time')
        fig, ax = plt.subplots(figsize=(14, 8))
        if 'GHI' in df.columns:
            ax.plot(df.index, df['GHI'], label='GHI')
        if 'DNI' in df.columns:
            ax.plot(df.index, df['DNI'], label='DNI')
        if 'DHI' in df.columns:
            ax.plot(df.index, df['DHI'], label='DHI')
        if 'Tamb' in df.columns:
            ax.plot(df.index, df['Tamb'], label='Tamb')
        ax.set_title('Time Series of GHI, DNI, DHI, and Tamb')
        ax.set_xlabel('Time')
        ax.set_ylabel('Values')
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("No 'Timestamp' column found for time series plotting.")

    # Plot Wind Analysis
    st.header('Wind Analysis')
    if 'WindSpeed' in df.columns and 'WindDirection' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.scatterplot(data=df, x='WindSpeed', y='WindDirection', ax=ax)
        ax.set_title('Wind Speed vs Wind Direction')
        ax.set_xlabel('Wind Speed')
        ax.set_ylabel('Wind Direction')
        st.pyplot(fig)
    else:
        st.write("Wind Speed and/or Wind Direction columns are missing for wind analysis.")

    # Plot Temperature and Humidity Analysis
    st.header('Temperature and Humidity Analysis')
    if 'Tamb' in df.columns and 'Humidity' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.scatterplot(data=df, x='Tamb', y='Humidity', ax=ax)
        ax.set_title('Temperature vs Humidity')
        ax.set_xlabel('Temperature')
        ax.set_ylabel('Humidity')
        st.pyplot(fig)
    else:
        st.write("Temperature and/or Humidity columns are missing for temperature-humidity analysis.")

else:
    st.write("Please upload a CSV file to start analysis.")
