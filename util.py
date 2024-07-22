import pickle
import json
import numpy as np

__cities = None
__data_columns = None
__model = None

def predict_temperature(city, year, month):
    try:
        city_index = __data_columns.index(city.lower())
    except:
        city_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = year
    x[1] = month
    if city_index >= 0:
        x[city_index] = 1

    return round(__model.predict([x])[0], 2)

def predict_temp_range(city, year, month, tolerance=1):
    predicted_temp = predict_temperature(city, year, month)
    lower_bound = predicted_temp - tolerance
    upper_bound = predicted_temp + tolerance

    return lower_bound, upper_bound

def load_temperature_model_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __model
    global __cities

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        print(f"Loaded data columns: {__data_columns}")  # Debug print
        __cities = __data_columns[2:]

    if __model is None:
        with open('./artifacts/Global_Temperature_of_Major_cities.pickle', 'rb') as f:
            __model = pickle.load(f)
            print("Model loaded successfully")  # Debug print

    print("Loading saved artifacts...done")

def get_city_names():
    return __cities

def get_model_columns():
    return __data_columns

if __name__ == '__main__':
    load_temperature_model_artifacts()
    # Test the functions
    print(predict_temperature('new york', 1990, 6))
    print(predict_temperature('los angeles', 1990, 6))
    print(predict_temperature('chicago', 1990, 6))
    print(predict_temperature('lagos', 1990, 6))


