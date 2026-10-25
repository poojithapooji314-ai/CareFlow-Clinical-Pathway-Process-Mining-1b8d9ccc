import pandas as pd

# Synthetic data only — not real patient data
events = pd.DataFrame([
    ["P001", "Registration", "2026-01-01 09:00"],
    ["P001", "Assessment", "2026-01-01 09:20"],
    ["P001", "Treatment", "2026-01-01 10:00"],
    ["P002", "Registration", "2026-01-01 09:10"],
    ["P002", "Assessment", "2026-01-01 09:40"],
    ["P002", "Treatment", "2026-01-01 10:30"],
])

events.columns = ["case_id", "activity", "timestamp"]
events["timestamp"] = pd.to_datetime(events["timestamp"])

journeys = events.groupby("case_id")["timestamp"].agg(
    start_time="min",
    end_time="max"
)

journeys["duration_minutes"] = (
    journeys["end_time"] - journeys["start_time"]
).dt.total_seconds() / 60

print("SYNTHETIC JOURNEY DURATION ANALYSIS")
print(journeys.to_string())

print("\nAverage journey duration:",
      round(journeys["duration_minutes"].mean(), 2), "minutes")
