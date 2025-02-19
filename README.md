House Price Prediction

Project Overview

This project aims to predict house prices based on various features such as the number of bedrooms, bathrooms, living area, lot size, location, and other important factors. Using machine learning techniques, we have built a regression model to estimate the house price accurately. The project also includes a deployment file to allow users to interact with the trained model locally.

Dataset Information

The dataset consists of houses sold in 2016, with various attributes:

Id: Unique identifier

Date: Date of sale

Price: Sale price (Target variable)

Bedrooms: Number of bedrooms

Bathrooms: Number of bathrooms

Living area: Square footage of the living space

Lot area: Square footage of the lot

Number of floors: Total number of floors

Waterfront: Whether the house is on a waterfront (1: Yes, 0: No)

Number of views: Special views count

Condition: House condition (1 to 5 scale)

Grade: House grading (1 to 13 scale based on foundation, drainage, etc.)

Area of the house: Square footage excluding basement

Area of Basement: Square footage of the basement

Built year: Year the house was built

Renovation year: Year of the latest renovation

Postal code: House location identifier

Living area after renovation: Living space after renovations

Lot area after renovation: Lot area after renovations

Schools nearby: Number of schools in the vicinity

Distance from the airport: Distance in kilometers from the nearest airport

Project Workflow

Data Preprocessing

Handling missing values

Feature engineering

Encoding categorical variables

Feature Selection

Identifying significant features affecting house prices

Model Selection & Training

Implementing various regression models including:

Linear Regression

Decision Tree

Random Forest

XGBoost

Hyperparameter tuning using GridSearchCV

Final Model: Gradient Boosting Regressor with an R² score of 0.75

Model Evaluation

Metrics used:

R-squared (R2 Score)

Mean Absolute Error (MAE)

Mean Squared Error (MSE)

Root Mean Squared Error (RMSE)

Technologies Used

Python

Libraries: NumPy, Pandas, Scikit-learn, XGBoost, Matplotlib, Seaborn, Statsmodels

Machine Learning Algorithms: Linear Regression, Decision Tree, Random Forest, Gradient Boosting

Deployment: Gradio for local UI-based interaction

Model Deployment

The deployment has been done using Gradio, which provides an interactive UI for users to input house details and get predicted prices.

How to Run the Deployment Locally

Ensure Python is installed along with the required libraries:

pip install gradio pandas numpy scikit-learn xgboost pickle5

Run the deployment script:

python House_Price_Prediction_Deployment.ipynb

Open the provided Gradio link in the browser and start predicting house prices.

Results

The final model was evaluated using various performance metrics, and the best model was selected based on the highest R-squared value and lowest error metrics. Gradient Boosting Regressor was chosen as the final model with an R² score of 0.75.

Future Improvements

Integration with cloud-based deployment platforms (e.g., Flask, FastAPI, or Streamlit for web apps)

Including additional features such as crime rates, school ratings, and economic indicators

Using deep learning approaches like ANN for improved performance

How to Contribute

Fork the repository

Create a new branch (feature-branch)

Make necessary changes and commit them

Push to your branch and create a pull request

Author & Acknowledgment

Developed by Suvrat Sanson as part of a machine learning project on real estate price prediction.
