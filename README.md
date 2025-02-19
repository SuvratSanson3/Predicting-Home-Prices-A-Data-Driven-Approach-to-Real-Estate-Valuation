House Price Prediction

📊 Project Workflow: House Price Prediction

1️⃣ Dataset Overview

Dataset Size: Houses sold in 2016 with various attributes.

Features:

Independent Variables: 'Bedrooms', 'Bathrooms', 'Living area', 'Lot area', 'Number of floors', 'Waterfront', 'Number of views', 'Condition', 'Grade', 'Area of the house', 'Area of Basement', 'Built year', 'Renovation year', 'Postal code', 'Living area after renovation', 'Lot area after renovation', 'Schools nearby', 'Distance from the airport'.

Dependent Variable: 'Price' (House sale price).

2️⃣ Data Preprocessing

Descriptive Analysis:

Summarized the dataset to understand distributions and relationships.

Data Cleaning:

Identified and removed missing or erroneous values.

Outlier Treatment:

Capped outliers using the Interquartile Range (IQR) method.

3️⃣ Regression Analysis Workflow

🔍 A. Assumptions Check for Linear Regression

Verified key assumptions:

Linearity

Homoscedasticity

Independence of errors

Normality of residuals

Absence of multicollinearity (treated using Variance Inflation Factor).

📈 B. Linear Regression Model

Performance:

R² (Train): 0.70

R² (Test): 0.68

🔄 C. Regularization Techniques

Ridge Regression:

R² (Train): 0.72

R² (Test): 0.70

Lasso Regression:

R² (Train): 0.72

R² (Test): 0.70

Elastic Net Regression:

R² (Train): 0.71

R² (Test): 0.69

🛠 D. Hyperparameter Tuning

Performed grid search to optimize hyperparameters for Ridge, Lasso, and Elastic Net models.

🚀 E. Gradient Boosting Regression

Fitted Gradient Boosting model for optimization.

Performance:

R² (Train): 0.76

R² (Test): 0.75

4️⃣ Key Results

Ridge, Lasso, and Elastic Net demonstrated similar performance with slight variations.

Gradient Boosting achieved the best performance with an R² score of 0.75 on the test set.

5️⃣ Conclusion

Regularized models (Ridge, Lasso, Elastic Net) achieved strong results, but Gradient Boosting Regressor provided the highest accuracy with an R² score of 0.75.

The project provides insights into the factors influencing house prices and demonstrates the effectiveness of advanced regression techniques in predictive modeling.

