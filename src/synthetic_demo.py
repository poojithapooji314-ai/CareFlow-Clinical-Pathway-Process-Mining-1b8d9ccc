
import pandas as pd

# Synthetic example only — not real patient data
events = pd.DataFrame([
    {"case_id": "P001", "activity": "Registration", "timestamp": "2026-01-01 09:00"},
    {"case_id": "P001", "activity": "Assessment", "timestamp": "2026-01-01 09:20"},
    {"case_id": "P001", "activity": "Treatment", "timestamp": "2026-01-01 10:00"},
    {"case_id": "P002", "activity": "Registration", "timestamp": "2026-01-01 09:10"},
    {"case_id": "P002", "activity": "Assessment", "timestamp": "2026-01-01 09:40"},
    {"case_id": "P002", "activity": "Treatment", "timestamp": "2026-01-01 10:30"},
])

events["timestamp"] = pd.to_datetime(events["timestamp"])
events = events.sort_values(["case_id", "timestamp"])

print("SYNTHETIC DEMO — NOT REAL PATIENT DATA")
print("Total cases:", events["case_id"].nunique())
print("Total events:", len(events))

print("\nEvents per activity:")
print(events["activity"].value_counts())

print("\nTime between consecutive activities:")
events["next_timestamp"] = (
    events.groupby("case_id")["timestamp"].shift(-1)
)
events["minutes_to_next_event"] = (
    events["next_timestamp"] - events["timestamp"]
).dt.total_seconds() / 60

print(events[
    ["case_id", "activity", "minutes_to_next_event"]
].to_string(index=False))
