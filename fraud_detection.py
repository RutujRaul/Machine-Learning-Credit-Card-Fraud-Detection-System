import pandas as pd
import pickle
from sklearn.ensemble import IsolationForest


df = pd.read_csv("data/creditcard_2023.csv")


selected_features = ["Amount", "V28", "V2", "V6", "V20", "V3"]
X = df[selected_features]


model = IsolationForest(contamination=0.02, random_state=42)
model.fit(X)


with open("models/fraud_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

print("✅ Model trained and saved as fraud_model.pkl")
