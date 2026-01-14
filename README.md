# Laptop Price Prediction using Machine Learning

This project predicts the price of a laptop based on its specifications using Machine Learning.
It covers the complete ML workflow from data preprocessing and feature engineering to model training and deployment readiness.

<img src = "laptop3.jpg" width="700">

# 📌 Project Overview

Laptop prices depend on multiple factors such as RAM, CPU, storage, display type, resolution, and weight.
This project uses a regression-based machine learning approach to estimate laptop prices accurately using these features.

# 🗂️ Dataset Description
The dataset contains information about laptops, including:

- Company
- TypeName
- Inches
- RAM
- Weight
- CPU details
- Screen resolution
- Touchscreen & IPS display
- Storage (HDD & SSD)
- Price (target variable)

## 📁 Project Sturcture
```
LAPTOP -PRICE-PREDICTION
├── laptop-price-prediction.ipynb   # Data analysis, feature engineering & model training
├── app.py                          # Streamlit web application
├── pipe.pkl                        # Trained machine learning pipeline
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation

```
  

# Machine Learning Pipeline

# 1. 🔍 Data Preprocessing
- Removed unnecessary index columns
- Handled duplicate and missing values
- Converted RAM and weight columns to numeric format
- Extracted touchscreen and IPS features
- Split screen resolution into horizontal and vertical pixels
- Calculated PPI (Pixels Per Inch)
- Extracted and categorized CPU brands


# 2. 🛠️ Feature Engineering

Key engineered features:
- Touchscreen (binary)
- IPS Display (binary)
- PPI calculated using screen resolution and size
- CPU Brand categorized as Intel Core / Other Intel / AMD
- Cleaned numeric columns for modeling

# 3. 🧠 Model Training
- Separated features (X) and target (y)
- Applied log1p transformation on price to reduce skewness
- Split data into 85% training and 15% testing
- Trained regression model using Scikit-learn

# 4. 📊 Exploratory Data Analysis (EDA)
- Visualized price distribution
- Analyzed correlations using heatmap
- Studied relationships between numerical features and price

# 5. 🚀 Deployment
- The trained model can be deployed using Streamlit, allowing users to:
- Select laptop specifications
- Predict laptop price in real-time
- View results in a clean, interactive UI

# 6. 🧪 Technologies Used
- Python
- Pandas
- NumPy
- Seaborn & Matplotlib
- Scikit-learn
- Streamlit



