import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('final_model_gb.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title('House Price Prediction')
st.write('Enter the details below to predict the house price.')

# User input fields
num_bed = st.number_input('Number of Bedrooms', min_value=1, max_value=10, value=3)
num_bath = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
liv_ar = st.number_input('Living Area (sqft)', min_value=500, max_value=10000, value=1500)
lot_ar = st.number_input('Lot Area (sqft)', min_value=500, max_value=50000, value=5000)
num_fl = st.number_input('Number of Floors', min_value=1, max_value=5, value=1)
wat_fr = st.number_input('Waterfront (1 = Yes, 0 = No)', min_value=0, max_value=1, value=0)
cond = st.number_input('Condition Rating (1-5)', min_value=1, max_value=5, value=3)
grade = st.number_input('Grade (1-13)', min_value=1, max_value=13, value=7)
house_ar = st.number_input('House Area (sqft)', min_value=500, max_value=10000, value=2000)
base_ar = st.number_input('Basement Area (sqft)', min_value=0, max_value=5000, value=500)
blt_yr = st.number_input('Year Built', min_value=1800, max_value=2025, value=2000)
liv_ar_ren = st.number_input('Living Area after Renovation (sqft)', min_value=500, max_value=10000, value=1500)
lot_ar_ren = st.number_input('Lot Area after Renovation (sqft)', min_value=500, max_value=50000, value=5000)
num_school = st.number_input('Nearby Schools', min_value=0, max_value=10, value=3)
airp_dist = st.number_input('Distance to Airport (miles)', min_value=1, max_value=50, value=10)
sell_mon = st.number_input('Selling Month (1-12)', min_value=1, max_value=12, value=6)
ren = st.number_input('Renovated (1 = Yes, 0 = No)', min_value=0, max_value=1, value=0)
view = st.number_input('View Score (0-4)', min_value=0, max_value=4, value=2)

# Predict function
def predict_price():
    input_data = np.array([[num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, 
                            blt_yr, liv_ar_ren, lot_ar_ren, num_school, airp_dist, sell_mon, ren, view]])
    pred = round(model.predict(input_data)[0], 3)
    return pred

if st.button('Predict Price'):
    price = predict_price()
    st.success(f'Estimated House Price: ${price:,}')
