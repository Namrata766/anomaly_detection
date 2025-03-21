from utils.data_loader import load_config, load_data, preprocess_data
from utils.anomaly_detector import train_baseline_model, detect_anomalies
from utils.root_cause_analysis import analyze_root_cause
import joblib

def main():
    # Load configuration
    config = load_config()

    # Load and preprocess historical data
    historical_data = load_data(config["data_paths"]["historical_data"])
    historical_data = preprocess_data(historical_data, config["time_column"], config["metric_column"], config["value_column"])

    # Train baseline model
    models = train_baseline_model(historical_data, config["metric_column"], config["value_column"])
    joblib.dump(models, config["model_path"])

    # Load and preprocess real-time data
    realtime_data = load_data(config["data_paths"]["realtime_data"])
    realtime_data = preprocess_data(realtime_data, config["time_column"], config["metric_column"], config["value_column"])

    # Detect anomalies
    anomalies = detect_anomalies(realtime_data, models, config["metric_column"], config["value_column"], config["anomaly_threshold"])
    print("Detected Anomalies:", anomalies)

    # Perform root cause analysis
    root_causes = analyze_root_cause(anomalies, historical_data, config["metric_column"], config["value_column"])
    print("Root Causes:", root_causes)

if __name__ == "__main__":
    main()