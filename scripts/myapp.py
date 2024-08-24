import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title of the dashboard
st.title("Simple Streamlit Dashboard")

# Display a text
st.write("This is a simple Streamlit dashboard example.")

# Create a slider widget for user interaction
slider_value = st.slider("Select a value", 0, 100, 50)

# Create some sample data
data = pd.DataFrame({
    'x': np.linspace(0, 100, 100),
    'y': np.sin(np.linspace(0, 100, 100) + slider_value / 10)
})

# Display the dataframe
st.write("Data Table:")
st.write(data)

# Plot the data using Matplotlib and display it
plt.figure(figsize=(10, 4))
plt.plot(data['x'], data['y'], label='sin(x + slider_value / 10)')
plt.title('Sine Wave with Slider Value Offset')
plt.xlabel('x')
plt.ylabel('sin(x + slider_value / 10)')
plt.legend()
st.pyplot(plt)

# Display a button and its response
if st.button("Click me!"):
    st.write("Button clicked!")
