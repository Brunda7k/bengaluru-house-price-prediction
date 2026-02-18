# Bengaluru Home Price Prediction

A **Data Science project** to predict **Bengaluru house prices** based on location, total square feet, BHK, and number of bathrooms.  
This project covers **data cleaning, feature engineering, outlier removal, model building, and prediction** using machine learning techniques.

---

## Key Highlights

- **Data Cleaning & Preprocessing:**  
  - Handling missing values  
  - Converting non-numeric square footage  
  - Standardizing locations  

- **Feature Engineering:**  
  - Created `price_per_sqft`  
  - Extracted `BHK` from size  
  - One-hot encoding for location  

- **Outlier Removal:**  
  - Removed extreme values based on price per square foot and BHK consistency  

- **Modeling & Prediction:**  
  - Linear Regression, Lasso, and Decision Tree Regressor  
  - GridSearchCV for hyperparameter tuning  
  - Predict function to estimate house prices given input features  

- **Visualization:**  
  - Scatter plots to analyze BHK vs price per sqft  
  - Histograms to understand distribution of prices and bathrooms  

---

## Folder Structure
BengaluruHomePrice/
├── app/
│   ├── main.py                  
│   ├── utils.py              
│   │   └── bengaluru_home_price_model.pickle
│   ├── static/                  
│   └── templates/              
├── notebooks/
│   └── Bengaluru_House_Price_Analysis.ipynb   
├── data/
│   └── Bengaluru_House_Data.csv               
├── columns.json 
