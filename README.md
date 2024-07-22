# Temperature Forecast Application

## Overview

The Temperature Forecast Application is a tool designed to predict and forecast temperatures for major global cities. Utilizing a DecisionTree model that achieved 97% accuracy, this application allows users to get temperature predictions and ranges for specific months and years.

## Features

- Predict the temperature for a specified city, month, and year.
- Get a temperature range prediction with a customizable tolerance.
- User-friendly interface built with Streamlit.
- Easy deployment using Flask and Gunicorn.

## Requirements

Ensure you have the following dependencies installed:

- flask>=2.0.0
- gunicorn>=20.1.0
- numpy>=1.21.0
- scipy>=1.7.0
- matplotlib>=3.4.0
- pandas>=1.3.0
- tpot>=0.11.0
- seaborn>=0.11.0
- cloudpickle>=1.6.0
- scikit-learn>=1.5.1
- joblib>=1.0.0
- flask-cors
- uvicorn

You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone https://github.com/Adekunle-Habeeb/Temperature-Prediction-App.git
cd Temperature-Prediction-App
```

### 2. Set Up Environment

Ensure you have Python installed. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Application

To run the application, use the following command:

```bash
streamlit run main.py
```

This will start the Streamlit application, and you can interact with the temperature prediction interface via your web browser.

### 4. Model Artifacts

Ensure you have the model artifacts (`columns.json` and `Global_Temperature_of_Major_cities.pickle`) in the `./artifacts/` directory.

## Application Usage

1. **Select City**: Use the sidebar to select the city for which you want to forecast the temperature.
2. **Enter Year and Month**: Provide the year and month for the forecast.
3. **Set Tolerance**: Adjust the tolerance value for range prediction (maximum 3.0).
4. **Predict Temperature**: Click the "Predict Temperature" button to get the estimated temperature.
5. **Predict Temperature Range**: Click the "Predict Temperature Range" button to get the temperature range forecast.

## Example

For example, to predict the temperature for New York in June 1990:

- Select "New York" as the city.
- Enter "1990" as the year.
- Enter "6" as the month.
- Click on "Predict Temperature" to get the forecast.

To get a temperature range with a tolerance of 1.0 degree:

- Select "New York" as the city.
- Enter "1990" as the year.
- Enter "6" as the month.
- Set the tolerance to "1.0".
- Click on "Predict Temperature Range" to get the range forecast.

## Footer

Developed by Habeeb | Temperature Prediction Model
