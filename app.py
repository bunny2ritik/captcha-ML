from flask import Flask, request, jsonify
import requests
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')  # Load the trained model

@app.route('/', methods=['GET'])
def home():
    return "Flask server is running"

@app.route('/api/fetch-and-analyze', methods=['GET'])
def fetch_and_analyze():
    try:
        url = "https://azcaptcha.com/demo"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.text
        data = extract_features(content)
        prediction = model.predict([data])
        return jsonify({'is_human': bool(prediction)})
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def extract_features(content):
    # Dummy feature extraction; replace with actual logic
    return [0] * len(model.feature_names_in_)  # Replace with actual feature extraction

if __name__ == '__main__':
    app.run(debug=True, port=8250)
