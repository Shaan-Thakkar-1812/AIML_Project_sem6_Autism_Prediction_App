
# Autism Predictor - Machine Learning Model

This project focuses on building and evaluating machine learning models to predict Autism Spectrum Disorder (ASD) based on structured health survey data. It addresses class imbalance using SMOTE and applies hyperparameter tuning to improve model performance.

---

## Project Structure
Autism_Predictor_App/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained machine learning model
├── test.csv                # Sample input data
├── AIMLproject.ipynb       # Jupyter notebook for model training
├── docs.md / README.md     # Documentation file
└── requirements.txt        # List of Python dependencies

## Install the required Python libraries:
pip install -r requirements.txt

## Key Libraries
pandas
numpy
scikit-learn
xgboost
imbalanced-learn
streamlit
matplotlib
seaborn

## How to Run

Step 1: Train the Model
Open and run all cells in AIMLproject.ipynb. This will:
Preprocess the data
Balance the classes using SMOTE
Perform cross-validation on 3 models
Tune hyperparameters using RandomizedSearchCV
Save the best model as best_model.pkl

Step 2: Run the Web App

Once the best model is saved, launch the Streamlit app:
streamlit run app.py

## Performance Evaluation
The best-performing model is selected based on highest cross-validation accuracy. The test performance is measured using:
Accuracy Score
Confusion Matrix
Classification Report