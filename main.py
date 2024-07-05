# from flask import Flask, request, jsonify, send_from_directory
# from flask_cors import CORS
# import util

# app = Flask(__name__, static_folder='client', static_url_path='')
# CORS(app)

# @app.route('/')
# def serve_home():
#     return send_from_directory(app.static_folder, 'index.html')

# @app.route('/get_city_names', methods=['GET'])
# def get_city_names():
#     cities = util.get_city_names()
#     return jsonify({'cities': cities})

# @app.route('/predict_temperature', methods=['POST'])
# def predict_temperature():
#     city = request.form.get('city')
#     year = int(request.form.get('year'))
#     month = int(request.form.get('month'))
#     estimated_temperature = util.predict_temperature(city, year, month)
#     return jsonify({'estimated_temperature': estimated_temperature})

# @app.route('/predict_temperature_range', methods=['POST'])
# def predict_temperature_range():
#     city = request.form.get('city')
#     year = int(request.form.get('year'))
#     month = int(request.form.get('month'))
#     tolerance = float(request.form.get('tolerance', 1.0))
#     lower_bound, upper_bound = util.predict_temp_range(city, year, month, tolerance)
#     return jsonify({'lower_bound': lower_bound, 'upper_bound': upper_bound})

# @app.route('/client/<path:path>')
# def static_files(path):
#     return send_from_directory('client', path)

# if __name__ == "__main__":
#     print("Starting Python Flask Server For Temperature Prediction...")
#     util.load_temperature_model_artifacts()
#     app.run(host='0.0.0.0', port=8000)



from flask import Flask, request, jsonify, send_from_directory
import util

app = Flask(__name__, static_folder='client', static_url_path='')

@app.route('/')
def serve_home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get_city_names', methods=['GET'])
def get_city_names():
    try:
        cities = util.get_city_names()
        response = jsonify({'cities': cities})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error fetching city names:", e)
        response = jsonify({'cities': None})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/predict_temperature', methods=['POST'])
def predict_temperature():
    try:
        city = request.form.get('city')
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        estimated_temperature = util.predict_temperature(city, year, month)
        response = jsonify({'estimated_temperature': estimated_temperature})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error predicting temperature:", e)
        response = jsonify({'estimated_temperature': None})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/predict_temperature_range', methods=['POST'])
def predict_temperature_range():
    try:
        city = request.form.get('city')
        year = int(request.form.get('year'))
        month = int(request.form.get('month'))
        tolerance = float(request.form.get('tolerance', 1.0))
        lower_bound, upper_bound = util.predict_temp_range(city, year, month, tolerance)
        response = jsonify({'lower_bound': lower_bound, 'upper_bound': upper_bound})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print("Error predicting temperature range:", e)
        response = jsonify({'lower_bound': None, 'upper_bound': None})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

@app.route('/client/<path:path>')
def static_files(path):
    return send_from_directory('client', path)

if __name__ == "__main__":
    print("Starting Python Flask Server For Temperature Prediction...")
    util.load_temperature_model_artifacts()
    app.run()
