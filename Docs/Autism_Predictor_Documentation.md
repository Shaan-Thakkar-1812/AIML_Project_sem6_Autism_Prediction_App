
# Autism Prediction App — Project Documentation

## Project Title:
**Autism Spectrum Disorder Prediction using Machine Learning**

## Description:
This project is a web-based application built using **Streamlit** that predicts the likelihood of an individual having Autism Spectrum Disorder (ASD). The prediction is based on a trained **Random Forest Classifier** that uses behavioral and demographic inputs.

## Objective:
To provide an intuitive and reliable tool that:
- Accepts input from users based on standard autism screening parameters.
- Predicts the probability of ASD in real-time.
- Helps in early detection and awareness of autism traits.

## Project Structure:
```
Autism_Predictor_App/
│
├── app.py                  # Main Streamlit application
├── model.pkl               # Trained machine learning model
├── test.csv                # Sample input data
├── AIMLproject.ipynb       # Jupyter notebook for model training
├── docs.md / README.md     # Documentation file
└── requirements.txt        # List of Python dependencies
```

## Features:
- Interactive form with all 19 required inputs.
- Real-time predictions using a trained model.
- Simple, clean user interface.
- Sample data input for quick testing.
- Works locally with minimal setup.

## Machine Learning Details:
- **Model Used:** Random Forest Classifier
- **Library:** Scikit-learn
- **Input Features:**
  - A1_Score to A10_Score
  - Age
  - Gender
  - Ethnicity
  - Jaundice (at birth)
  - Family member with ASD
  - Who completed the screening
- **Output:** Binary classification indicating autism likelihood.

## Technologies Used:

| Technology      | Purpose                            |
|----------------|------------------------------------|
| Python          | Programming Language               |
| Streamlit       | Web Application Interface          |
| Scikit-learn    | Model Training & Prediction        |
| Pandas          | Data Processing                    |
| Pickle          | Model Serialization                |

## How to Run the Application:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/autism-predictor-app.git
   cd autism-predictor-app
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Sample Input (from `test.csv`):

| A1_Score | A2_Score | A3_Score | A4_Score | A5_Score | A6_Score | A7_Score | A8_Score | A9_Score | A10_Score | Age | Gender | Ethnicity | Jaundice | Family_mem_with_ASD | Who_completed_the_test |
|----------|----------|----------|----------|----------|----------|----------|----------|----------|-----------|-----|--------|-----------|----------|----------------------|--------------------------|
| 1        | 0        | 1        | 0        | 1        | 1        | 0        | 1        | 0        | 1         | 22  | Male   | White     | No       | Yes                  | Parent                   |

## Expected Output:
- **Low chance of Autism**
- **High chance of Autism**

## Future Enhancements:
- Add visualizations for user analysis.
- Model comparison dashboard.
- Exportable prediction reports.
- Deploy on cloud (e.g., AWS, Azure, Streamlit Cloud).

## Author:
**Shaan Thakkar**  
Computer Science Undergraduate  
Machine Learning and Management Enthusiast
