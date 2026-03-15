# Insurance Cost Prediction using Machine Learning

## Project Overview
This project is a Machine Learning web application that predicts insurance cost based on user details such as age, BMI, number of children, smoking status, and region.

The system compares multiple machine learning algorithms and displays predictions to determine the best performing model.

## Technologies Used
- Python
- Machine Learning
- Flask
- HTML
- CSS
- Scikit-learn
- Pandas
- NumPy

## Dataset
The dataset used is the **Insurance dataset**, which contains medical cost information for training and testing the model.

## Project Interface

### Before Prediction
![Before Prediction](before_prediction.png)

### After Prediction
![After Prediction](after_prediction.png)

## Files in the Project
- `app.py` – Flask application that runs the web server
- `insurance_model.pkl` – Trained machine learning model
- `insurance.csv` – Dataset used for training
- `index.html` – Web interface for user input
- `style.css` – Styling for the web page
- `best_model_name.txt` – Stores the name of the best performing model

## How to Run the Project

### 1. Clone the repository
```
git clone https://github.com/your-username/insurance-cost-prediction.git
```

### 2. Navigate to the project folder
```
cd insurance-cost-prediction
```

### 3. Install required libraries
```
pip install pandas numpy scikit-learn flask
```

### 4. Run the application
```
python app.py
```

### 5. Open the web application
Open your browser and go to:

```
http://127.0.0.1:5000
```

The application will open in your browser where you can enter user details and get the predicted insurance cost.
