import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = None
try:
    model = joblib.load("model.pkl")  # Load the trained model
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'model.pkl' is in the correct location.")
except Exception as e:
    st.error(f"Error loading model: {e}")

# Prediction function
def prediction(model, num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, blt_yr, liv_ar_ren, lot_ar_ren,
               num_school, airp_dist, sell_mon, ren, view):
    if model is None:
        raise ValueError("Model not loaded. Cannot make predictions.")
    input_data = np.array([[num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, blt_yr, liv_ar_ren, lot_ar_ren,
                            num_school, airp_dist, sell_mon, ren, view]])
    pred = round(model.predict(input_data)[0], 3)
    return pred

# Main app
def main():
    st.title("House Price Prediction")

    # User inputs
    num_bed = st.number_input("Enter Number of Bedrooms", min_value=1, value=3)
    num_bath = st.number_input("Enter Number of Bathrooms", min_value=1, value=2)
    liv_ar = st.number_input("Enter the Living Area (sq. ft.)", min_value=1, value=1500)
    lot_ar = st.number_input("Enter the Lot Area (sq. ft.)", min_value=1, value=5000)
    num_fl = st.number_input("Enter the Number of Floors", min_value=1, value=2)
    wat_fr = st.selectbox("Is a Waterfront Present?", ['Yes', 'No'])
    wat_fr = 1 if wat_fr == 'Yes' else 0
    cond = st.slider("Condition of the House (1 - Poor to 5 - Excellent)", 1, 5, value=3)
    grade = st.slider("Grade of the House (4 - Low to 13 - High)", 4, 13, value=7)
    house_ar = st.number_input("Enter the Area of the House (without Basement, sq. ft.)", min_value=1, value=1200)
    base_ar = st.number_input("Enter the Basement Area (sq. ft.)", min_value=0, value=800)
    blt_yr = st.number_input("Enter the Year the House was Built", min_value=1900, max_value=2025, value=2000)
    liv_ar_ren = st.number_input("Enter the Living Area After Renovation (sq. ft.)", min_value=1, value=1500)
    lot_ar_ren = st.number_input("Enter the Lot Area After Renovation (sq. ft.)", min_value=1, value=5000)
    num_school = st.selectbox("Number of Schools Nearby", [0, 1, 2, 3], index=1)
    airp_dist = st.number_input("Enter the Distance from the Airport (miles)", min_value=0.1, value=10.0)
    sell_mon = st.slider("Selling Month (1 - January to 12 - December)", 1, 12, value=6)
    ren = st.selectbox("Is the House Renovated?", ['Yes', 'No'])
    ren = 1 if ren == 'Yes' else 0
    view = st.selectbox("Does the House Have a View?", ['Yes', 'No'])
    view = 1 if view == 'Yes' else 0

    # Making prediction
    if st.button("Predict"):
        if model is None:
            st.error("Model not loaded. Cannot make predictions.")
        else:
            try:
                price = prediction(model, num_bed, num_bath, liv_ar, lot_ar, num_fl, wat_fr, cond, grade, house_ar, base_ar, blt_yr, liv_ar_ren, lot_ar_ren,
                                   num_school, airp_dist, sell_mon, ren, view)
                st.success(f"Predicted House Price: ${price}")
            except Exception as e:
                st.error(f"Error during prediction: {e}")

if __name__ == '__main__':
    main()
