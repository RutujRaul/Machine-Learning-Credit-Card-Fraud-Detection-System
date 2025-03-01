import pickle
import numpy as np
from flask import Flask, request, render_template, jsonify

with open("models/fraud_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        features = [
            float(request.form.get('Amount', 0)),
            float(request.form.get('V28', 0)),
            float(request.form.get('V2', 0)),
            float(request.form.get('V6', 0)),
            float(request.form.get('V20', 0)),
            float(request.form.get('V3', 0))
        ]
        
        
        input_data = np.array(features).reshape(1, -1)
        
        
        prediction = model.predict(input_data)
        
        
        result = "Fraud" if prediction[0] == -1 else "Legit"
        
        return render_template('index.html', prediction_text=f'Transaction is: {result}')
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
