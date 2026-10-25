import pandas as pd

# Synthetic demonstration data only
events = pd.DataFrame([
	["P001", "Registration", "2026-01-01 09:00"],
	["P001", "Assessment", "2026-01-01 09:20"],
	["P001", "Treatment", "2026-01-01 10:00"],
	["P002", "Registration", "2026-01-01 09:00"],
	["P002", "Assessment", "2026-01-01 09:30"],
	["P002", "Treatment", "2026-01-01 11:00"],
])

events.columns = ["case_id", "activity", "timestamp"]
events["timestamp"] = pd.to_datetime(events["timestamp"])
events = events.sort_values(["case_id", "timestamp"])

events["next_activity"] = events.groupby("case_id")["activity"].shift(-1)
events["next_time"] = events.groupby("case_id")["timestamp"].shift(-1)
events["delay_minutes"] = (
	events["next_time"] - events["timestamp"]
).dt.total_seconds() / 60

transitions = events.dropna(subset=["next_activity"])

summary = (
	transitions.groupby(["activity", "next_activity"])["delay_minutes"]
	.agg(["mean", "max", "count"])
	.reset_index()
	.sort_values("mean", ascending=False)
)

print("SYNTHETIC BOTTLENECK ANALYSIS")
print(summary.to_string(index=False))
print("\nNote: Longer time gaps are potential delays,")
print("not proof of clinical problems.")
