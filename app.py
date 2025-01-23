import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    with open('final_model_gb.pkl', 'rb') as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")

# Prediction function
def prediction(num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, blt_yr, liv_ar_ren, lot_ar_ren,
              num_school, airp_dist, sell_mon, ren, view):
    input_data = [[num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, blt_yr, liv_ar_ren, lot_ar_ren,
                  num_school, airp_dist, sell_mon, ren, view]]
    pred = round(model.predict(input_data)[0], 3)
    return pred

# Main app
def main():
    st.title("House Price Prediction")

    # User inputs
    num_bed = st.number_input("Enter Number of Bedrooms", min_value=1)
    num_bath = st.number_input("Enter Number of Bathrooms", min_value=1)
    liv_ar = st.number_input("Enter the Living area", min_value=1)
    lot_ar = st.number_input("Enter the Lot Area", min_value=1)
    num_fl = st.number_input("Enter the Number of Floors", min_value=1)
    wat_fr = st.selectbox("Is a waterfront present?", ['Yes', 'No'])
    wat_fr = 1 if wat_fr == 'Yes' else 0
    cond = st.slider("What is the Condition of the House?", 1, 5)
    grade = st.slider("What is the Grade of the House?", 4, 13)
    house_ar = st.number_input("Enter the area of the House (without Basement)", min_value=1)
    base_ar = st.number_input("Enter the area of the Basement", min_value=1)
    blt_yr = st.number_input("Enter the year the house was built", min_value=1900, max_value=2025)
    liv_ar_ren = st.number_input("Enter the Living area after Renovation", min_value=1)
    lot_ar_ren = st.number_input("Enter the Lot Area after Renovation", min_value=1)
    num_school = st.selectbox("What is the number of schools nearby?", [0, 1, 2, 3])
    airp_dist = st.number_input("Enter the distance from Airport", min_value=1)
    sell_mon = st.slider("Which is the Selling Month?", 1, 12)
    ren = st.selectbox("Is the House renovated?", ['Yes', 'No'])
    ren = 1 if ren == 'Yes' else 0
    view = st.selectbox("Does the house have a view?", ['Yes', 'No'])
    view = 1 if view == 'Yes' else 0

    # Making prediction
    if st.button("Predict"):
        price = prediction(num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, blt_yr, liv_ar_ren, lot_ar_ren,
                          num_school, airp_dist, sell_mon, ren, view)
        st.success(f"Predicted House Price: ${price}")

if __name__ == '__main__':
    main()
