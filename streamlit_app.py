import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate movement speed
def calculate_movement_speed(scale_factor, dexterity_multiplier, dexterity, base_speed):
    return scale_factor * np.log(dexterity_multiplier * dexterity + 1) + base_speed

# Streamlit app
st.title('Movement Speed Calculator')

# Sidebar for input parameters
st.sidebar.header('Input Parameters')
scale_factor = st.sidebar.slider('Scale Factor', 0.0, 10.0, 1.0, 0.1)
dexterity_multiplier = st.sidebar.slider('Dexterity Multiplier', 0.0, 10.0, 1.0, 0.1)
dexterity = st.sidebar.slider('Dexterity', 1, 100, 10)
base_speed = st.sidebar.slider('Base Speed', 0, 100, 10)

# Calculate movement speed
movement_speed = calculate_movement_speed(scale_factor, dexterity_multiplier, dexterity, base_speed)

# Display movement speed
st.write(f'Movement Speed: {movement_speed:.2f}')

# Plot graph
dexterities = np.arange(1, 101, 1)
movement_speeds = calculate_movement_speed(scale_factor, dexterity_multiplier, dexterities, base_speed)

plt.figure(figsize=(10, 6))
plt.plot(dexterities, movement_speeds, label='Movement Speed')

plt.xlabel('Dexterity')
plt.ylabel('Movement Speed')
plt.title('Movement Speed Based on Dexterity')
plt.legend()
plt.grid(True)

st.pyplot(plt.gcf())

