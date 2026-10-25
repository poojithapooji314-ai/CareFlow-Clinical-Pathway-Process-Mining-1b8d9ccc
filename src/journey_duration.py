import pandas as pd

<<<<<<< HEAD
data = {
	"case_id": ["P001", "P001", "P002", "P002"],
	"timestamp": [
		"2026-01-01 09:00",
		"2026-01-01 10:00",
		"2026-01-01 09:10",
		"2026-01-01 10:30",
	],
}

df = pd.DataFrame(data)
df["timestamp"] = pd.to_datetime(df["timestamp"])

duration = df.groupby("case_id")["timestamp"].agg(
	start="min",
	end="max",
)

duration["duration_minutes"] = (
	duration["end"] - duration["start"]
).dt.total_seconds() / 60

print("Synthetic Journey Duration Analysis")
print(duration.to_string())
=======
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
>>>>>>> b45407098a6dfb6c1bf9d07161132bf75447aba6
