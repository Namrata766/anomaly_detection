import numpy as np
from sklearn.ensemble import IsolationForest
import joblib

def train_baseline_model(historical_data, metric_column, value_column):
    metrics = historical_data[metric_column].unique()
    models = {}
    for metric in metrics:
        data = historical_data[historical_data[metric_column] == metric][value_column].values.reshape(-1, 1)
        model = IsolationForest(contamination=0.01)
        model.fit(data)
        models[metric] = model
    return models

def detect_anomalies(realtime_data, models, metric_column, value_column, threshold):
    anomalies = []
    for metric, model in models.items():
        data = realtime_data[realtime_data[metric_column] == metric][value_column].values.reshape(-1, 1)
        if len(data) > 0:
            scores = model.decision_function(data)
            predictions = model.predict(data)
            for i, (score, prediction) in enumerate(zip(scores, predictions)):
                if prediction == -1 or abs(score) > threshold:
                    anomalies.append({
                        "timestamp": realtime_data.index[i],
                        "metric_name": metric,
                        "value": data[i][0],
                        "score": score
                    })
    return anomalies