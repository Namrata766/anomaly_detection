def analyze_root_cause(anomalies, historical_data, metric_column, value_column):
    root_causes = []
    for anomaly in anomalies:
        metric = anomaly["metric_name"]
        historical_values = historical_data[historical_data[metric_column] == metric][value_column]
        mean = historical_values.mean()
        std = historical_values.std()
        if anomaly["value"] > mean + 2 * std:
            root_causes.append(f"High value anomaly detected for {metric}. Possible cause: Unexpected spike.")
        elif anomaly["value"] < mean - 2 * std:
            root_causes.append(f"Low value anomaly detected for {metric}. Possible cause: Unexpected drop.")
    return root_causes