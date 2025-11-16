Oil Spill Detection Using Machine Learning

This project predicts and classifies oil spills in marine environments using machine learning models trained on satellite image data and AIS datasets. It supports multiple ML models and provides a simple web interface for prediction.

Features
*Uses 49+ features from the oil spill dataset
*Supports multiple machine learning models:
*Random Forest
*SVC
*XGBoost
*Logistic Regression
*Clean Flask-based backend
*User-friendly UI with sliders for input
*Trained models stored as .joblib files
*Real-time prediction output

Tech Stack
*Backend: Python, Flask
*ML Models: RandomForest, SVC, Logistic Regression, XGBoost
*Frontend: HTML, CSS (Bootstrap), JavaScript
*Tools/Libs: Pandas, NumPy, Scikit-learn, Joblib

Models Used
*Random Forest → Strong performance on tabular features
*SVC → High accuracy on high-dimensional data
*XGBoost → Gradient boosting model for better precision
*Logistic Regression → Baseline model
*Each model is trained on all 49 features and saved as .joblib files.

Goal
To build a fully functional web-based system that can take input parameters, process them through trained models, and predict whether an area shows signs of an oil spill.
